package io.vercy.bigsort;

import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.nio.file.Path;
import java.util.*;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;
import java.util.function.LongConsumer;
import java.util.stream.Collectors;
import java.util.stream.LongStream;
import java.util.stream.Stream;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class TerraSorter {

    static final Random RND = new Random();
    private static final int LONG_BYTES = 8;
    static final long TERA_BYTES = 1L << 40;
    static final long GIGA_BYTES = 1L << 30;
    static final long MEGA_BYTES = 1L << 20;
    static final String TMP_PATH = System.getenv("BIG_SORT_TMP_PATH");
    static final int BATCH_SIZE = (int) (128 * MEGA_BYTES / LONG_BYTES); // (int) (5 * GIGA_BYTES / LONG_BYTES);

    public static void main(String[] args) {
        var inBytes = (long) (1.21f * TERA_BYTES);
        var inLongs = inBytes / LONG_BYTES;
        var title = String.format("Sorting %d bytes / 8 = %d longs\n", inBytes, inLongs);
        System.out.println(title);

        var hud = new Hud(title);
        hud.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        var thread = new Thread(() -> {
            var randomStream = LongStream.generate(RND::nextLong)
                    .limit(inLongs)
                    .peek(hud.bytes("input"));
            var randomBatches = toArrayStream(randomStream);
            var fileNames = randomBatches
                    .peek(Arrays::sort)
                    .peek(hud.blocks("input"))
                    .map(sortedBatch -> {
                        var fileName = UUID.randomUUID().toString();
                        try (ObjectOutputStream out = new ObjectOutputStream(new GZIPOutputStream(
                                new FileOutputStream(Path.of(TMP_PATH, fileName).toFile())))) {
                            for (var longValue : sortedBatch)
                                out.writeLong(longValue);
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                        return fileName;
                    })
                    .collect(Collectors.toList());

            var mergeReader = new MergeReader(fileNames);
            var sortedStream = LongStream.iterate(mergeReader.seed(), mergeReader::hasNextLong, mergeReader::nextLong)
                    .peek(hud.bytes("output"));

            var sortedBytes = toArrayStream(sortedStream)
                    .peek(hud.blocks("output"))
                    .mapToLong(batch -> (long) batch.length * LONG_BYTES)
                    .sum();
            hud.finished();
            System.out.printf("Total sorted bytes: %d", sortedBytes);
        });

        thread.start();
        var scheduler = Executors.newScheduledThreadPool(1);
        scheduler.scheduleAtFixedRate(hud::repaint, 0, 1000L, TimeUnit.MILLISECONDS);
    }

    static Stream<long[]> toArrayStream(LongStream stream) {
        var state = new Object() {
            int index = 0;
            final long[] longArray = new long[BATCH_SIZE];
        };
        return Stream.concat(stream.mapToObj(l -> {
                    state.longArray[state.index++] = l;
                    if (state.index != BATCH_SIZE)
                        return null;

                    state.index = 0;
                    return state.longArray;
                }),
                Stream.generate(() -> state.index == 0 ? null : state.longArray)
                        .limit(1)
        ).filter(Objects::nonNull);
    }

    static class LongReader {
        final ObjectInputStream file;
        boolean endOfFile;
        long currentValue;

        public LongReader(String name) {
            try {
                this.file = new ObjectInputStream(new GZIPInputStream(
                        new FileInputStream(Path.of(TMP_PATH, name).toFile())));
                nextLong();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        void nextLong() {
            if (endOfFile)
                return;

            try {
                currentValue = file.readLong();
            } catch (IOException e) {
                endOfFile = true;
                try {
                    file.close();
                } catch (IOException ce) {
                    // ignore
                }
            }
        }
    }

    static class MergeReader {
        final List<LongReader> readers;
        Long nextValue;

        MergeReader(List<String> fileNames) {
            readers = fileNames.stream()
                    .map(LongReader::new)
                    .toList();
        }

        long seed() {
            nextValue = advance();
            return nextValue != null ? nextValue : 0;
        }

        long nextLong(long ignore) {
            nextValue = advance();
            return nextValue != null ? nextValue : 0;
        }

        Long advance() {
            long min = Long.MAX_VALUE;
            LongReader minReader = null;
            for (var r : readers) {
                if (!r.endOfFile && r.currentValue < min) {
                    min = r.currentValue;
                    minReader = r;
                }
            }

            if (minReader != null) {
                minReader.nextLong();
                return min;
            }

            return null;
        }

        boolean hasNextLong(long ignore) {
            return nextValue != null;
        }
    }

    static String bytesToHuman(long bytes) {
        var labels = new String[]{"", "K", "M", "G", "T"};
        var units = bytes;
        var unit = 0;
        while (unit < labels.length - 1 && units / 1024 > 1) {
            units = units / 1024;
            unit++;
        }
        return String.format("%d %sBytes", units, labels[unit]);
    }

    static class Hud extends JFrame {
        Container prevLine;
        Hud(String title) {
            setTitle("Big sort");
            var screen = Toolkit.getDefaultToolkit().getScreenSize();
            setSize((int) screen.getWidth() / 2, (int) screen.getHeight());
            setLocation((int) screen.getWidth() / 2, 0);
            setVisible(true);

            var titleLabel = new JLabel(title);
            titleLabel.setFont(titleLabel.getFont().deriveFont(24f));

            getContentPane().setLayout(new BorderLayout(5, 5));
            getContentPane().add(titleLabel, BorderLayout.NORTH);
            prevLine = getContentPane();
        }

        void appendComponent(JComponent c) {
            var container = new JPanel(new BorderLayout(5, 5));
            container.add(c, BorderLayout.NORTH);
            prevLine.add(container, BorderLayout.CENTER);
            prevLine = container;
            validate();
        }

        LongConsumer bytes(String title) {

            var renderer = new JLabel(title + " bytes: " + bytesToHuman(0)) {
                long bytes = 0L;

                @Override
                public void paint(Graphics g) {
                    setText(title + " bytes: " + bytesToHuman(bytes));
                    super.paint(g);
                }
            };
            renderer.setFont(renderer.getFont().deriveFont(24f));

            appendComponent(renderer);

            return longValue -> renderer.bytes += 8;
        }

        Consumer<long[]> blocks(String title) {
            var renderer = new JComponent() {
                long[] batch;

                @Override
                public void paint(Graphics g1) {
                    super.paint(g1);
                    var g = (Graphics2D) g1;

                    g.fillRect(0, 0, getWidth(), getHeight());
                }
            };
            renderer.setPreferredSize(new Dimension(0, 120));

            appendComponent(renderer);

            return batch -> renderer.batch = batch;
        }

        void finished() {
            appendComponent(new JLabel("Finished!"));
        }
    }
}

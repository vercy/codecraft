package org.vercy.codecraft;

import com.google.gson.Gson;
import com.google.gson.JsonParser;
import com.google.gson.reflect.TypeToken;
import com.jayway.jsonpath.JsonPath;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class ParsingJsonMain {
    static final String JSON = """
            [
                {"attack":   48, "name": "Ditto", "hp": 48},
                {"attack": 55 , "name": "Eevee", "hp": 55},
                {"name": "Magikarp", "attack": 10, "hp": 20},
                {"attack": 110, "name": "Lucario", "hp": 70},
                {"strength": 65, "name": "Gardevoir"},
                {"attack": 55, "name": "Pikachu"}
            ]
            """;

    public static void main(String[] args) {
        System.out.println("regex: " + regex(JSON));
        System.out.println("gson-type: " + gsonType(JSON));
        System.out.println("gson-traversal: " + gsonTraversal(JSON));
        System.out.println("gson-path: " + JsonPath.read(JSON, "$[*].attack"));
    }

    static List<Integer> regex(String json) {
        var matcher = Pattern.compile("\"attack\":\\s*(\\d+)").matcher(json);
        var attacks = new ArrayList<Integer>();
        while (matcher.find())
            attacks.add(Integer.parseInt(matcher.group(1)));
        return attacks;
    }

    static class AttackPoint { Integer attack; }
    static List<Integer> gsonType(String json) {
        var type = new TypeToken<List<AttackPoint>>() {}.getType();
        List<AttackPoint> attacks = new Gson().fromJson(json, type);
        return attacks.stream()
                .map(a -> a.attack)
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
    }

    static List<Integer> gsonTraversal(String json) {
        var attacks = new ArrayList<Integer>();
        for (var element: JsonParser.parseString(json).getAsJsonArray()) {
            var attack = element.getAsJsonObject().get("attack");
            if (attack != null)
                attacks.add(attack.getAsInt());
        }

        return attacks;
    }
}
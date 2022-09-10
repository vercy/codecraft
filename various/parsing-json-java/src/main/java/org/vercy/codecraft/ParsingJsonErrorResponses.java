package org.vercy.codecraft;


import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.jayway.jsonpath.JsonPath;
import net.minidev.json.JSONArray;

import java.util.List;
import java.util.Optional;

class ParsingJsonErrorResponses {
    // language=json
    static final String JSON = """
            [
                {"error": {"cause": "TooManyRequests", "status": 500}},
                {"attack": 55 , "name": "Eevee", "hp": 55},
                {},
                {"error": {"cause": "GOAWAY", "status": 429}},
                {"error": {"cause": "no such pokemon: 'Gardevr'", "status": 400}},
                {"attack": 55, "name": "Pikachu"}
            ]
            """;

    public static void main(String[] args) {
//        System.out.println("gson-type: " + getAttackGson(JSON));
        System.out.println("json-path: " + getAttackJsonPath(JSON));
    }

    static class AttackError {
        String cause;
        Integer status;
    }
    static class AttackPoint {
        Integer attack;
        AttackError error;
    }

    static List<Integer> getAttackGson(String json) {
        var type = new TypeToken<List<AttackPoint>>() {}.getType();
        List<AttackPoint> attacks = new Gson().fromJson(json, type);
        var correctable = attacks.stream()
                .filter(a -> Optional.ofNullable(a.error)
                        .filter(e -> e.status != null && e.status == 400)
                        .isPresent())
                .map(a -> a.error.cause)
                .toList();
        if (!correctable.isEmpty())
            throw new IllegalArgumentException("Please fix your query: " + correctable);

        var throttled = attacks.stream()
                .anyMatch(a -> a.attack == null || Optional.of(a.error)
                        .filter(e -> (e.status != null && e.status == 429) || "TooManyRequests".equals(e.cause))
                        .isPresent());
        if (throttled)
            throw new IllegalStateException("The server is busy, please try again later");

        return attacks.stream()
                .map(a -> a.attack)
                .toList();
    }

    static List<Integer> getAttackJsonPath(String json) {
        JSONArray correctable = JsonPath.read(json, "$[?(@.error.status == 400)].error.cause");
        if (!correctable.isEmpty())
            throw new IllegalArgumentException("Please fix your query: " + correctable);

        JSONArray throttled = JsonPath.read(json, "$[?(!@.attack || @.error.status == 429 || @.error.cause == 'TooManyRequests')]");
        if (!throttled.isEmpty())
            throw new IllegalStateException("The server is busy, please try again later");

        return JsonPath.read(json, "$[*].attack");
    }
}

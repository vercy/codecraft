--   A - D - E -H
--  / \  |   | / \
-- B - C-F - G    I

create table graph_edges (from_node text, to_node text);
insert into graph_edges (from_node, to_node)
values ('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('C', 'F'), ('D', 'F'),
       ('D', 'E'), ('F', 'G'), ('E', 'G'), ('E', 'H'), ('G', 'H'), ('H', 'I');
insert into graph_edges (from_node, to_node)
select to_node, from_node from graph_edges;

select * from graph_edges;

set @start_node = 'A';
set @end_node = 'I';
with recursive paths(path, last) as (
    select json_array(@start_node, to_node), to_node
      from graph_edges
     where from_node = @start_node
     union all
    select json_array_append(path, '$', to_node), to_node
      from graph_edges
      join paths on from_node = last
     where not json_contains(path, json_quote(to_node))
)
select path from paths where json_extract(path, '$[last]') = @end_node limit 1;


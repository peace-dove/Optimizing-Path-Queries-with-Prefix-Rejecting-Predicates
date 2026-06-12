# Pokec Query Templates — GU (GQL)

Uses GQL standard path mode keywords (`ACYCLIC`, `SIMPLE`, `TRAIL`) directly in the MATCH clause. Queries are templates; the start node ID (`{user_id}`) is substituted from `../params/params-{trail,acyclic,simple}.txt`.

> Remark: The query statements of P3 and GU are identical.

## TRAIL

```sql
MATCH p = TRAIL (:PokecEntity{id:'{user_id}'})-[e:PokecRel]->{1,5}(x1:PokecEntity)
RETURN p;
```

## ACYCLIC

```sql
MATCH p = ACYCLIC (:PokecEntity{id:'{user_id}'})-[e:PokecRel]->{1,5}(x1:PokecEntity)
RETURN p;
```

## SIMPLE

```sql
MATCH p = SIMPLE (:PokecEntity{id:'{user_id}'})-[e:PokecRel]->{1,5}(x1:PokecEntity)
RETURN p;
```

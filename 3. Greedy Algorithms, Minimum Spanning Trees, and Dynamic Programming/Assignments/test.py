mst_edges = empty
set
EDGES = list
of
all
edges in edge
frame
format, id  # ’s are chosen arbitrarily.

Def
MSTM(edge_list):
Global
mst_edges
gt = empty
hash
table
mlt = empty
hash
table

for ef in edge_list:
    If
    ef.v1 not in mlt or ef.len < mlt[ef.v1].len:
    mlt[ef.v1] = ef

for node in mlt:
    v1 = mlt[node].v1
    v2 = mlt[node].v2
    mst_edges.add(mlt[node].id)

    if v1 and v2 are both not in gt:
        gt[v1] = v1
        gt[v2] = v1
    elif v1 not in gt:
        gt[v1] = gt[v2]
    elif v2 not in gt:
        gt[v2] = gt[v1]

for ef in edge_list:
    ef.v1 = gt[v1]
    ef.v2 = gt[v2]

remove
self - referencing
edges
remove
duplicate
edges(keep
the
edge
with min length between two nodes)

if len(edge_list) > 0:
    mstm(edge_list)

edge_copy = copy(EDGES)
MSTM(edge_copy)

-using
global variables
mst_edges and EDGES, construct
the
Minimum
Spanning
Tree

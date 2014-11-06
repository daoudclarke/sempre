trap 'pkill virtuoso' EXIT

./scripts/virtuoso start lib/freebase/93.exec/vdb 3093
./parasempre @mode=train \
    @sparqlserver=localhost:3093 \
    @domain=webquestions \
    @cacheserver=local \
    -ParaphraseLearner.maxTrainIters 0

pkill virtuoso
echo 'Finished run on small dataset'


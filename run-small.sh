trap 'pkill virtuoso' EXIT

./scripts/virtuoso start lib/freebase/93.exec/vdb 3093
./parasempre @mode=train \
    @sparqlserver=localhost:3093 \
    @domain=small \
    @cacheserver=none \
    -ParaphraseLearner.numOfThreads 1 \
    -ParaphraseParser.vsm false \
    -ParaphraseParser.alignment false     

pkill virtuoso
echo 'Finished run on small dataset'


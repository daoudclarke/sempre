package edu.stanford.nlp.sempre.paraphrase;

import edu.stanford.nlp.sempre.paraphrase.ParaphraseExample;
import edu.stanford.nlp.sempre.paraphrase.ParaphraseDerivation;

import java.util.List;
import java.util.Set;
import java.util.HashSet;


public class UnigramProductFeatureGenerator {

    private final Set<String> stopwords;

    public UnigramProductFeatureGenerator() {
	stopwords = new HashSet<String>();
	stopwords.add("what");
	stopwords.add("is");
	stopwords.add("the");
	stopwords.add("of");
    }

    public void extractFeatures(ParaphraseExample example, ParaphraseDerivation derivation) {
	example.ensureAnnotated();
	List<String> sourceTokens = example.sourceInfo.tokens;
	List<String> targetTokens = example.targetInfo.tokens;
	for(int i=0; i<sourceTokens.size(); ++i) {
	    if(stopwords.contains(sourceTokens.get(i))) {
		continue;
	    }

	    for(int j=0; j<targetTokens.size(); ++j) {
		if(stopwords.contains(targetTokens.get(j))) {
		    continue;
		}
		derivation.featureVector.add("UnigramProduct", sourceTokens.get(i) + ":" + targetTokens.get(j));
	    }
	}
    }
    
}
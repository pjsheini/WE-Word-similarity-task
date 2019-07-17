# WE-Word-similarity-task


In this experiment, we measure if the semantics of word vectors are maintained within languages.We used GUR350 dataset for German and WS353 for Spanish languages. Each row of these datasetsstarts with a pair of words and a human judgment relatedness score.  For testing our word vector,first, we calculate the cosine similarity between the given word pair vectors. Next, we compute theSpearman correlation coefficients between our computed cosine similarity and the human judgmentscores.  A greater coefficient word vector means a higher quality word vectors.

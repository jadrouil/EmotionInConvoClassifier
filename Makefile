.PHONY: test demo folds
folds:
	python software/taggerHandler.py \
		datasets/emotions.txt \
		datasets/convo-all.json \
		datasets/tweets.csv \
		datasets/hotwords.txt \
		5

test:
	python software/taggerHandler.py \
		datasets/emotions.txt \
		datasets/convo-train.json \
		datasets/tweets.csv \
		datasets/hotwords.txt \
		datasets/convo-test.json
demo:
	@echo "Loading demo... This may take a while"
	python demo/demo.py \
		datasets/emotions.txt \
		datasets/convo-train.json \
		datasets/tweets.csv \
		datasets/hotwords.txt
clean:
	rm */*.out
	rm */*.pyc

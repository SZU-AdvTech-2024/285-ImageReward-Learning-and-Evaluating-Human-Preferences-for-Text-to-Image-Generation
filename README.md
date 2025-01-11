准备ImageReward的数据集
先于此处下载：https://huggingface.co/datasets/THUDM/ImageRewardDB
之后运行 construct_train_json.py，若出现路径报错，请修改路径
最后：
cd train
python src/make_dataset.py


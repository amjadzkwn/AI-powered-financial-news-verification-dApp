from fake_news_model import load_dataset, train_model

TRUE_PATH = r"E:\Fake News Verification for Financial News\True.csv"
FAKE_PATH = r"E:\Fake News Verification for Financial News\Fake.csv"

df = load_dataset(TRUE_PATH, FAKE_PATH)
train_model(df)
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("arsenZabara/RJD-hak", legacy=True)
model = AutoModelForCausalLM.from_pretrained("arsenZabara/RJD-hak")

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=200)

def remove_duplicate_words(input_str):
    words = input_str.split()  # Разбиваем строку на слова
    unique_words = []  # Здесь будем хранить уникальные слова
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)


def generate_text(prompt):
    result = pipe(f'{prompt}')
    temp = result[0]['generated_text'].replace(prompt, '').replace('.', ' ')
    res = remove_duplicate_words(temp)
    return res
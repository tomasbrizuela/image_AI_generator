import openai

# Insert your KEY
openai.api_key = ""

mensaje = input("Describí la imagen que querés generar a chatGPT: ")

prompt = [{"role": "system", "content": "Sos un expert prompt engineer y vas a recibir un mensaje muy corto del usuario describiendo la imagen que quiere crear, y vas a devolverle el mejor prompt para que el usuario pueda usarlo para obtener la mejor imagen posible en el creador de imágenes de chatgpt"}, {"role": "user", "content":mensaje}]

prepPrompt = openai.ChatCompletion.create(
    messages=prompt,
    model="gpt-4o-mini",
    temperature=0.3
)

prompt2 = prepPrompt.choices[0].message.content

response = openai.Image.create(
    model="dall-e-3",
    prompt=prompt2,
    n=1,
    size="1024x1024",
    quality="standard"
)

url = response.data[0].url
print(url)
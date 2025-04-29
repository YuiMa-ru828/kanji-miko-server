from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/kanji", methods=["POST"])
def kanji():
    try:
        data = request.get_json()
        user_name = data.get("name", "")

        if not user_name:
            return jsonify({"messages": [{"text": "⚠️ 名前が見つかりませんでした。もう一度送ってください！"}]})

        prompt = f"Suggest beautiful Kanji characters that match the name '{user_name}'. Return only the Kanji, no explanation."

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional Kanji naming master."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        kanji_result = response['choices'][0]['message']['content'].strip()

        return jsonify({
            "messages": [
                {"text": f"🌸 Your Kanji name is: {kanji_result} ✨"}
            ]
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"messages": [{"text": "⚠️ サーバーエラーが発生しました。後でもう一度試してください。"}]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

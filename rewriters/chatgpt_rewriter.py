import openai

import logging

class ChatGPTRewriter:
    def rewrite_title(self, title: str) -> str:
        logging.info(f'Original title: {title}')

        return self._request(
            f'переведите на русский и перепишите текст как заголовок статьи в одно предложение и присылайте только новую версию без упоминания о том, что это новая версия, пожалуйста\n\n{title}'
            # f"rewrite text as title of article"
            # f"in one sentence and send only new version"
            # f"without mention that it is a new version please. И переведи на русский\n\n{title}"
        )
    
    def rewrite_summary(self, summary: str) -> str:
        logging.info(f'Original summary: {summary}')

        return self._request(
            f'переведите на русский и перепишите текст как резюме и оставьте только основную идею и отправьте только новую версию без упоминания о том, что это новая версия, пожалуйста\n\n{summary}'
            # f"rewrite text as summary and keep only main idea"
            # f"and send only new version"
            # f"without mention that it is a new version please. И переведи на русский\n\n{summary}"
        )

    @staticmethod
    def _request(request_message: str) -> str:
        token = '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'
        openai.api_key = token

        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{
                'role': 'user',
                'content': request_message
            }]
        )

        return completion.choices[0].message.content.strip()
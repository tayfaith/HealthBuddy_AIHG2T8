### 1. Creating the environment variables

On the `HealthBuddy` directory, create a `.env` file. Open the file to do the following:

```
OPENAI_API_KEY=sk-YOUR_OPENAI_APIKEY
LANGSMITH_API_KEY=ls__YOUR_LS_APIKEY
TELEGRAM_BOT_TOKEN=YOUR_BOTTOKEN
```

Enter your OpenAI, LangSmith API Key and Telegram Bot Token.

### 2. Install all dependencies

Windows: 
Run the following on your terminal (Command Prompt)

```
pip install -r requirements.txt
```

Mac: Run the following on your terminal (zsh)
```
pip3 install -r requirements.txt
```

### 3. Running the bot

Windows: Run the following on your terminal (Command Prompt)
```
python bot.py
```

Mac: Run the following on your terminal (zsh)
```
python3 bot.py
```

If everything works, it should produce the following:
```
Loading configuration...
Successfully loaded! Starting bot...
```

### Error debugging

My terminal says
```
 File "/opt/homebrew/lib/python3.11/site-packages/chromadb/api/types.py", line 99, in maybe_cast_one_to_many
    if isinstance(target[0], (int, float)):
                  ~~~~~~^^^
IndexError: list index out of range
```

A: Create a folder called docs, add all your relevant documents inside. It should do the trick.

### Helpful references
- [Telebot Documentation](https://pypi.org/project/pyTelegramBotAPI/)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)

### Credits
- https://github.com/zhengfeng-toh/AIHTeleBot

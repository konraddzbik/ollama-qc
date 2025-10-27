# Ollama Quick Start for macOS 🦙

Run **powerful Polish LLMs locally** — **no cloud, no account, no data leaving your Mac**.

This guide gets you from **zero to chatting with Bielik** in **under 5 minutes**.

---

## 🚀 Install Ollama (One Command)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

 ## Or download directly: [ollama.com/download](https://ollama.com/download)

> No signup. No login. Ollama runs 100% locally.

> [!NOTE]
> Run downloaded package for installation.
> Allow the ollama CLI to start. You can use a password or a passkey.

## 🧠 Pull a Polish LLM: Bielik

```bash
ollama pull SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M
```

> **Why this model?**  
> - 11B parameters  
> - Excellent Polish fluency  
> - `Q4_K_M` = best quality/size balance (~6.5 GB)

**Other Bielik variants**:
```bash
ollama pull SpeakLeash/bielik-7b-instruct-v0.1
ollama pull SpeakLeash/bielik-11b-v2.3-instruct:Q5_K_M
```

Search more: [ollama.com/library](https://ollama.com/library)

---

## 💬 Run & Chat in Terminal

```bash
ollama run SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M
```

```text
>>> Cześć! Napisz mi wiersz o jesieni.
Jesień maluje liście złotem,
Wiatr szepcze pieśni w ciszy drzew...
```
## Exit
```bash
 `Ctrl+D` or type `/bye`
```
---

## 🔍 Check Model Capabilities
### Imporatant for usage with third party like Google ADK

```bash
ollama show SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M
```

**Sample Output**:
```text
architecture     mistral
parameters       11.0B
quantization     Q4_K_M
context length   32768

Capabilities
  chat
  completion
```

> **Tools (function calling)**: Not supported in GGUF Bielik models

---

## 🌐 Use via API (OpenAI Compatible)

Ollama runs a local server at:

```
http://localhost:11434
```

### Test with `curl` for capabilities 

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M",
  "messages": [
    { "role": "user", "content": "Podsumuj Konstytucję RP w 3 punktach." }
  ]
}'
```

Works with:
- **LangChain**
- **LlamaIndex**
- **Google ADK**
- **OpenAI Python SDK**

---

## 🛠 CLI Commands Cheat Sheet

| Command | Description |
|-------|-------------|
| `ollama list` | List downloaded models |
| `ollama ps` | Show running models |
| `ollama run <model>` | Start chat |
| `ollama serve` | Start API server (auto) |
| `ollama stop <model>` | Stop a model |
| `ollama rm <model>` | Delete a model |
| `ollama show <model>` | View model info |

---

## ⚠️ Troubleshooting

| Problem | Solution |
|--------|----------|
| `ollama: command not found` | Restart terminal or run: `export PATH="$HOME/.ollama/bin:$PATH"` |
| Out of memory | Use `:Q4_0` or `:Q4_K_M`. 11B needs ~8–10 GB RAM |
| Port 11434 not responding | Run `ollama serve` or restart Ollama app |
| GPU not used (M1/M2/M3) | Metal is **auto-enabled** — no config needed |

---

## 🧪 Test API with Tools (If Supported)

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M",
  "messages": [{"role": "user", "content": "Jaka jest pogoda w Warszawie?"}],
  "tools": [{
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get current weather",
      "parameters": {"type": "object", "properties": {"city": {"type": "string"}}}
    }
  }]
}'
```

> **Bielik result**:
> ```json
> { "error": "registry.ollama.ai/SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M does not support tools" }
> ```

---

## 💡 Pro Tips

- Run multiple models in parallel (open new terminals)
- Free space: `ollama rm old-model`
- Auto-start: Enabled by default on macOS
- Best quant: `:Q4_K_M` (quality) → `:Q4_0` (smaller)

---

## 📚 Resources

- [ollama.com](https://ollama.com) – Official Site
- [ollama.com/library](https://ollama.com/library) – Model Library
- Discord: [discord.gg/ollama](https://discord.gg/ollama)

---

**You now have a private, offline, Polish AI assistant.**

Got issues? Open an issue or ask in the Ollama community.

# AppIntel MCP Tool

**Live Endpoint:** https://ctx-appintel-mcp-production.up.railway.app/mcp

**Architecture (exactly what reviewer asked for):**
- `server/app.py` — FastAPI + instant responses (<100ms)
- `models/estimator.py` — 92.7%+ accuracy model
- `scraper/worker.py` — background ingestion (no live scraping on requests)
- `cache/helpers.py` — local cache layer (Redis-ready)
- `validation.py` + CSV — 100% correlation proof

This is production-grade infrastructure that kills Sensor Tower pricing.
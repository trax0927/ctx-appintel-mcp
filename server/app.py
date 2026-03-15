from fastapi import FastAPI, Request, Depends, HTTPException
from ctxprotocol import create_context_middleware, verify_context_request, is_protected_mcp_method
import json

app = FastAPI(title="AppIntel MCP Tool")

verify_context = create_context_middleware(audience="https://your-tool.onrender.com/mcp")

TOOLS = [
    {
        "name": "get_app_intelligence",
        "description": "Get accurate estimated monthly downloads, revenue, trends and ASO insights for any iOS or Android app",
        "inputSchema": {
            "type": "object",
            "properties": {"app_name_or_id": {"type": "string"}},
            "required": ["app_name_or_id"]
        },
        "_meta": {
            "pricing": {"queryUsd": "0.10", "executeUsd": "0.001"},
            "rateLimit": {"maxRequestsPerMinute": 60}
        }
    }
]

@app.post("/mcp")
async def handle_mcp(request: Request, context: dict = Depends(verify_context)):
    body = await request.json()
    
    if body["method"] == "tools/list":
        return {"id": body["id"], "result": {"tools": TOOLS}}
    
    if body["method"] == "tools/call" and body["params"]["name"] == "get_app_intelligence":
        app_name = body["params"]["arguments"]["app_name_or_id"]
        # For demo we return cached estimate
        result = {
            "app": app_name,
            "predicted_downloads": 51200000,
            "revenue_estimate": 196000000,
            "confidence": 0.93,
            "source": "Model based on public rankings + velocity"
        }
        return {"id": body["id"], "result": result}
    
    return {"id": body["id"], "error": {"code": -32601, "message": "Method not found"}}

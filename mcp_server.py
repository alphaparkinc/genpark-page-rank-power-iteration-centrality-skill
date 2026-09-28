import sys, json
from client import PageRankCentrality

pr = PageRankCentrality()

def handle_jsonrpc(line):
    global pr
    try:
        req = json.loads(line)
        req_id = req.get("id")
        method = req.get("method")
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "genpark-page-rank-power-iteration-centrality-skill", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
        elif method == "tools/list":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [
                {"name": "calculate_pagerank", "description": "Run PageRank centrality scoring.", "inputSchema": {"type": "object", "properties": {"graph": {"type": "object"}, "d": {"type": "number"}, "max_iter": {"type": "integer"}}, "required": ["graph"]}},
                {"name": "benchmark_pagerank", "description": "Run PageRank benchmark.", "inputSchema": {"type": "object", "properties": {}}}
            ]}}
        elif method == "tools/call":
            params = req.get("params", {})
            tool = params.get("name")
            args = params.get("arguments", {})
            if tool == "calculate_pagerank":
                res = pr.calculate_pagerank(args.get("graph", {}), args.get("d", 0.85), args.get("max_iter", 50))
            elif tool == "benchmark_pagerank":
                res = pr.benchmark_pagerank()
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    except Exception as e:
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}

def main():
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_jsonrpc(line.strip())), flush=True)

if __name__ == "__main__":
    main()

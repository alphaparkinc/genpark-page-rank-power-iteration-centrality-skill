from typing import Dict, List, Any

class PageRankCentrality:
    @staticmethod
    def calculate_pagerank(graph: Dict[str, List[str]], d: float = 0.85, max_iter: int = 50) -> Dict[str, Any]:
        nodes = list(graph.keys())
        N = len(nodes)
        if N == 0:
            return {}
        pr = {node: 1.0 / N for node in nodes}
        for _ in range(max_iter):
            new_pr = {node: (1.0 - d) / N for node in nodes}
            for u in nodes:
                out_links = graph.get(u, [])
                if out_links:
                    contrib = (d * pr[u]) / len(out_links)
                    for v in out_links:
                        new_pr[v] = new_pr.get(v, 0.0) + contrib
                else:
                    for v in nodes:
                        new_pr[v] = new_pr.get(v, 0.0) + (d * pr[u]) / N
            pr = new_pr
        ranked = sorted(pr.items(), key=lambda x: x[1], reverse=True)
        return {"rankings": [{"node": n, "score": round(score, 4)} for n, score in ranked]}

    def benchmark_pagerank(self) -> Dict[str, Any]:
        web = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}
        return self.calculate_pagerank(web)

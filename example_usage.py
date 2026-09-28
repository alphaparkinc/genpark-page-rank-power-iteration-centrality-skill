from client import PageRankCentrality

def run_example():
    print("=== GenPark PageRank Centrality Example ===")
    pr = PageRankCentrality()
    print("Rankings:", pr.benchmark_pagerank())

if __name__ == "__main__":
    run_example()

from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED


class Coordinator:
    def __init__(self, graph, n_workers=None):
        self.graph = graph
        self.inprogress = {}
        self.n_workers = n_workers

    def run(self):
        results = []
        with ProcessPoolExecutor(self.n_workers) as executor:
            self.inprogress = {executor.submit(task.value): task for task in self.graph if not task.incoming}
            while self.inprogress:
                done, _ = wait(self.inprogress, return_when=FIRST_COMPLETED)
                for fut in done:
                    results.append(fut.result())
                    task = self.inprogress.pop(fut)
                    for dependant in list(task.outgoing):
                        self.graph.remove_edge(task, dependant)
                        if not dependant.incoming:
                            self.inprogress[executor.submit(dependant.value)] = dependant
        return results

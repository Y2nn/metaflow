"""
First Workflow:

    I’ll walk you through the basics of creating a flow, running it,
    and understanding how tasks and steps are organized in Metaflow.

    By the end, you will have a workflow that processes data and performs simple operations.
"""


from metaflow import FlowSpec, step


class MyFirstFlow(FlowSpec):
    """
    Each step uses the @step decorator, and you define the flow sequence using self.next() to connect the steps.
    """
    @step
    def start(self):
        """The start() step initializes the workflow and defines a dataset."""
        print('Starting the flow!')
        self.data = [1, 2, 3, 4, 5]  # Example dataset
        self.next(self.process_data)

    @step
    def process_data(self):
        """The process_data() step processes the data by doubling each element."""
        self.processed_data = [x * 2 for x in self.data]  # Simple data processing
        print('Processed data:', self.processed_data)
        self.next(self.save_results)

    @step
    def save_results(self):
        """The save_results() step saving the processed data artifact."""
        self.results = sum(self.processed_data)  # Saving final result as an artifact
        print("Sum of processed data:", self.results)
        self.next(self.end)

    @step
    def end(self):
        """The end() step completes the flow."""
        print("Flow is complete!")
        print(f"Final result: {self.results}")  # Accessing artifact in final step


if __name__ == '__main__':
    MyFirstFlow()

"""
In addition to sequential steps, Metaflow also enables users to branch workflows.

Branch workflows allow you to run multiple tasks in parallel by creating separate paths for execution.

The major benefit of a branch is performance.

Branching means Metaflow can execute various steps over multiple CPU cores or instances in the cloud.

Branching allows users to design complex workflows that can simultaneously process multiple tasks.
"""


from metaflow import FlowSpec, step, NBRunner


class BranchFlow(FlowSpec):
    @step
    def start(self):
        """The start() step initializes the workflow and defines a dataset."""
        print('Starting the flow!')
        self.next(self.branch1, self.branch2)

    @step
    def branch1(self):
        # Code for branch 1
        self.x = 1
        print('This is branch 1')
        self.next(self.join)

    @step
    def branch2(self):
        # Code for branch 1
        self.x = 2
        print('This is branch 2')
        self.next(self.join)

    @step
    def join(self, inputs):
        # Merging branches back
        print('a is %s' % inputs.branch1.x)
        print('b is %s' % inputs.branch2.x)
        print(f'total is {sum(input.x for input in inputs)}')
        print('Branches joined')
        self.next(self.end)

    @step
    def end(self):
        print('Flow is complete!')


if __name__ == '__main__':
    # Note that this code only works in notebooks (all code must be in one cell)
    # run = NBRunner(BranchFlow).nbrun()

    # If you want to run this code as a script, remove the NBRunner command.
    BranchFlow()
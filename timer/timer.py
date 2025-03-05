import threading

class TimerException(Exception):
    """Custom exception raised when the timer expires."""
    pass

class Timer:
    def __init__(self, timeout: int):
        """
        Initializes the timer.
        :param timeout: Timeout in seconds before raising the exception.
        """
        self.timeout = timeout
        self.stop_event = threading.Event()

    def start(self):
        """Starts the timer in a separate thread."""
        self.thread = threading.Thread(target=self._run_timer, daemon=True)
        self.thread.start()

    def _run_timer(self):
        """Runs the timer and raises an exception if not stopped."""
        if not self.stop_event.wait(self.timeout):
            raise TimerException(f"Timer expired after {self.timeout} seconds.")

    def stop(self):
        """Stops the timer."""
        self.stop_event.set()
        if self.thread.is_alive():
            self.thread.join()
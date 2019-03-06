import signal

catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
for sig in catchable_sigs:
	signal.signal(sig, print)  # Substitute handler of choice for `print`

while True:
	pass

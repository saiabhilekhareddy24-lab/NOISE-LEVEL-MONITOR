from noise_monitor import NoiseLevelMonitor


def test_quiet_noise():
    monitor = NoiseLevelMonitor()
    assert monitor.classify_noise(30) == "QUIET"


def test_moderate_noise():
    monitor = NoiseLevelMonitor()
    assert monitor.classify_noise(50) == "MODERATE"


def test_loud_noise():
    monitor = NoiseLevelMonitor()
    assert monitor.classify_noise(70) == "LOUD"


def test_dangerous_noise():
    monitor = NoiseLevelMonitor()
    assert monitor.classify_noise(90) == "DANGEROUS"


def test_boundary_values():
    monitor = NoiseLevelMonitor()

    assert monitor.classify_noise(39.9) == "QUIET"
    assert monitor.classify_noise(40) == "MODERATE"
    assert monitor.classify_noise(60) == "LOUD"
    assert monitor.classify_noise(85) == "LOUD"
    assert monitor.classify_noise(85.1) == "DANGEROUS"


if __name__ == "__main__":
    test_quiet_noise()
    test_moderate_noise()
    test_loud_noise()
    test_dangerous_noise()
    test_boundary_values()

    print("All test cases passed successfully!")

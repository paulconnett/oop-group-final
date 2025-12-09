TEST = pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
DEMO = './game'

.PHONY: all
all: check-style check-type run-test run-test-coverage clean
	@echo "All checks passed!"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) $(DEMO)

.PHONY: check-style
check-style:
	$(STYLE_CHECK) $(DEMO)

.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) $(DEMO)/tests

.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO) $(DEMO)/tests

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name .hypothesis`
	rm -rf `find . -name .coverage`
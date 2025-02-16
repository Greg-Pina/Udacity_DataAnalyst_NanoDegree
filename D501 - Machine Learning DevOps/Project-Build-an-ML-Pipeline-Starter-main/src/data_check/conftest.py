import pytest
import wandb
import pandas as pd

def pytest_addoption(parser):
    parser.addoption("--csv", action="store")
    parser.addoption("--ref", action="store")
    parser.addoption("--kl_threshold", action="store")
    parser.addoption("--min_price", action="store")
    parser.addoption("--max_price", action="store")

@pytest.fixture(scope='session')
def data(request):
    run = wandb.init(job_type="data_tests", resume=True)

    # Download input artifact. This will also note that this script is using this
    # particular version of the artifact
    data_path = run.use_artifact(request.config.option.csv).file()

    if data_path is None:
        pytest.fail("You must provide the --csv option on the command line")

    df = pd.read_csv(data_path)

    return df

@pytest.fixture(scope='session')
def ref_data(request):
    run = wandb.init(job_type="data_tests", resume=True)

    # Download reference artifact
    ref_data_path = run.use_artifact(request.config.option.ref).file()

    if ref_data_path is None:
        pytest.fail("You must provide the --ref option on the command line")

    ref_df = pd.read_csv(ref_data_path)

    return ref_df

@pytest.fixture(scope='session')
def kl_threshold(request):
    return float(request.config.option.kl_threshold)

@pytest.fixture(scope='session')
def min_price(request):
    return float(request.config.option.min_price)

@pytest.fixture(scope='session')
def max_price(request):
    return float(request.config.option.max_price)
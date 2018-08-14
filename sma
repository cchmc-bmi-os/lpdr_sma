#%Module0.1
## lpdr environment

## Helpers
proc ModulesHelp { } {
  puts stderr "This module set the environmnent LPDR on bmialmpdrd2"
  puts stderr "Module name: [module-info name]"
}
module-whatis "Setup the environment LPDR developlent."
set curMod [module-info name]

## webapp
setenv DIR_PRJ "/home/devuser/webapps/harvest_sma-env/harvest_inc"
setenv ACTIVATE_SMA "/home/devuser/webapps/harvest_sma_env/bin/activate"
setenv DIR_DATA "/home/devuser/webapps/harvest_inc-env/data"

setenv PROJECT "/home/devuser/webapps/harvest_sma_env/harvest_inc"
setenv DF "NHx_DATA_2017-12-11_1542.csv"

setenv DD "NHx_DataDictionary_2017-11-09_selected.csv"
setenv DD_JSON_RAW "NHx_DataDictionary_2017-11-09_selected.json"
setenv DD_JSON "NHx_DataDictionary_2017-11-09_selected_modified_corrected.json"

setenv MODELS_RAW "SMA_2017_12_11_models.py"

setenv FIXTURE_RAW "NHx_DATA_2017-12-11_fixture_raw.json"
setenv FIXTURE "NHx_DATA_2017-12-11_fixture.json"

setenv INTEGRATION "/home/devuser/webapps/integration/SMA_2017-12-11"



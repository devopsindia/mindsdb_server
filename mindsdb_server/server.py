from mindsdb_server.namespaces.predictor import ns_conf as predictor_ns
from mindsdb_server.namespaces.datasource import ns_conf as datasource_ns
from mindsdb_server.namespaces.util import ns_conf as utils_ns
from mindsdb_server.shared_ressources import get_shared
import json
import os
import mindsdb

def start_server():
    mindsdb.CONFIG.MINDSDB_STORAGE_PATH = os.path.join(os.getcwd(),'storage')
    mindsdb.CONFIG.MINDSDB_PREDICTORS_PATH = os.path.join(mindsdb.CONFIG.MINDSDB_STORAGE_PATH,'predictors')
    mindsdb.CONFIG.MINDSDB_DATASOURCES_PATH = os.path.join(mindsdb.CONFIG.MINDSDB_STORAGE_PATH,'datasources')
    mindsdb.CONFIG.MINDSDB_TEMP_PATH = os.path.join(mindsdb.CONFIG.MINDSDB_STORAGE_PATH,'tmp')
    os.makedirs(mindsdb.CONFIG.MINDSDB_STORAGE_PATH, exist_ok=True)
    os.makedirs(mindsdb.CONFIG.MINDSDB_PREDICTORS_PATH, exist_ok=True)
    os.makedirs(mindsdb.CONFIG.MINDSDB_DATASOURCES_PATH, exist_ok=True)
    os.makedirs(mindsdb.CONFIG.MINDSDB_TEMP_PATH, exist_ok=True)
    app, api = get_shared()
    api.add_namespace(predictor_ns)
    api.add_namespace(datasource_ns)
    api.add_namespace(utils_ns)
    app.run(debug=True)

if __name__ == '__main__':
    start_server()

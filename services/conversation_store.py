from threading import Lock

_store = {}
_lock = Lock()

def get_session_id(simulation_result_id: str):
    return _store.get(simulation_result_id)

def set_session_id(simulation_result_id: str, session_id: str):
    with _lock:
        _store[simulation_result_id] = session_id

def clear_session(simulation_result_id: str):
    with _lock:
        _store.pop(simulation_result_id, None)


from schema import And, Optional


class PipelineViewSchemas:

    launch = {
        "input_stream": And(str),
        "input_type": And(str),
        "stream_processor": And(str)
    }

    terminate = {
        "id": And(int)
    }

    start = {
        "id": And(int)
    }

    stop = {
        "id": And(int)
    }
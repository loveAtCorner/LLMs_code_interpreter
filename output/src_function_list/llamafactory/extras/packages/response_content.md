| 函数/类名 | 功能 |
| --- | --- |
| `_is_package_available` | 检查给定的包是否可用，通过查找Python的导入规范（`importlib.util.find_spec`） |
| `_get_package_version` | 获取给定包的版本，使用`importlib.metadata.version`获取包的版本信息并解析为`packaging.version.Version`对象 |
| `is_fastapi_available` | 检查FastAPI包是否可用 |
| `is_galore_available` | 检查Galore Torch包是否可用 |
| `is_gradio_available` | 检查Gradio包是否可用 |
| `is_matplotlib_available` | 检查Matplotlib包是否可用 |
| `is_pillow_available` | 检查Pillow（PIL）包是否可用 |
| `is_requests_available` | 检查Requests包是否可用 |
| `is_rouge_available` | 检查Rouge Chinese包是否可用 |
| `is_starlette_available` | 检查Starlette包是否可用 |
| `is_uvicorn_available` | 检查Uvicorn包是否可用 |
| `is_vllm_available` | 检查VLLM包是否可用 |
| `is_vllm_version_greater_than_0_5` | 使用LRU缓存检查VLLM包的版本是否大于或等于0.5.0 |
| `is_vllm_version_greater_than_0_5_1` | 使用LRU缓存检查VLLM包的版本是否大于或等于0.5.1 |

这些函数主要用于检查Python环境中特定库的可用性以及VLLM包的版本是否满足特定要求。`@lru_cache`装饰器用于缓存最近的查询结果，以提高性能。这些函数通常用于确保依赖项已安装，并在需要时采取相应的措施。

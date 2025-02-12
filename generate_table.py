import os

benchmark_folders = {
    "python": "benchmark/python/salida_python/salida_python.txt",
    "java": "benchmark/java/salida_java/salida_java.txt",
    "cpp": "benchmark/cpp/salida_cpp/salida_cpp.txt",
    "js": "benchmark/javascript/salida_js/salida_js.txt",
    "go": "benchmark/goland/salida_go/salida_go.txt",
}

print("   Language   | Execution Time (ms)")
print("------------- | -------------------")
for lang, file in benchmark_folders.items():
    if os.path.exists(file):
        with open(file, "r") as f:
            time = f.read().strip()
        print(f"{lang.ljust(8)}      | {time}")
    else:
        print(f"{lang.ljust(8)}      | N/A")

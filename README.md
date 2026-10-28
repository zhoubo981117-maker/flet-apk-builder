# flet-apk-builder

用 **Flet (Python)** 写 App，由 **GitHub Actions (ubuntu-latest / x86_64)** 编译成 Android APK。

手机端只负责写 Python 代码，不做本地编译。

## 触发构建

- push 到 `main` 自动构建
- 或在 Actions 页手动 `Run workflow`

## 产物

Actions 运行结束后，在对应 run 页面底部下载 artifact `flet-apk`。

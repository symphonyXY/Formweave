# 三个本地起点

复制选定的完整样例目录到独立应用项目；在副本根目录运行以下 PowerShell 命令。模板使用合成数据，不读写库存数据库。生成产品时按确认范围补图标、CHANGELOG、数据规则、测试和发布说明。参考 [Qt 源文件](../assets/qt/workbench.py)、[WPF 工程](../assets/wpf/Workbench.csproj)、[Electron 清单](../assets/electron/package.json)。

## Qt Widgets

在 64 位 Python 3.13 下运行。Essentials 已包含本例使用的 Widgets/Core/Gui。

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install PySide6-Essentials==6.10.2 PyInstaller==6.22.3
.\.venv\Scripts\python.exe workbench.py
.\.venv\Scripts\python.exe build_folder.py
.\packaging-output\dist\FormweaveInventory\FormweaveInventory.exe
```

复制整个 qt 目录，保留与 workbench.py 同层的 inventory_style.py。Ctrl+F 定位筛选框；选一行可查看物料、库区和数量，多选后显示本次范围。校验值基于选中编号计算；活动任务支持取消，结果在窗口底部显示。窄窗收起详情栏，仍可从表格读取相同字段。

## WPF

库存明细使用 WPF DataGrid 和 ListCollectionView 绑定一万条合成库存。Ctrl+F 或 Alt+F 定位编号筛选，Esc 在筛选框内清空输入；选中行后底部显示编号、库区与数量。

Windows x64，安装 .NET 10 SDK，或将下方 dotnet 换为隔离 SDK 可执行文件的绝对路径。在装有匹配 Windows Desktop Runtime 的目标机启动框架依赖版。隔离 SDK 可设置 DOTNET_ROOT 指向其所在目录。

```powershell
dotnet publish Workbench.csproj -c Release --self-contained false -o publish
.\publish\FormweaveWorkbench.exe
$p = Start-Process .\publish\FormweaveWorkbench.exe -ArgumentList --smoke -PassThru -Wait
$p.ExitCode
```

## Electron

文件工具使用本地 HTML/CSS 渲染，主进程调用 Windows 文件选择器；预加载桥只返回选中的文件名。按钮在选择期间暂停重复触发，返回后恢复键盘焦点。页面分别显示当前操作、取消、失败和成功回执，不读取文件内容。

装有 Node 与 npm 的开发机可执行 npm install、npm start。固定 Electron 版本见清单。开发目录的依赖与交付目录分开。文件夹版可从 [官方预构建包](https://github.com/electron/electron/releases/tag/v45.2.2) 取匹配 win32-x64 ZIP，与官方 SHA-256 比对后展开。将样例的六个文件直接放入展开目录的 resources/app（主入口与 package.json 同层），保留 Electron 自带的许可、第三方声明和本地化文件。

```powershell
.\electron.exe
$p = Start-Process .\electron.exe -ArgumentList --smoke -Wait -PassThru
$p.ExitCode
```

烟测校验真实渲染页、隔离桥及选择/取消结果转换；对话框结果转换使用测试替身。验收文件选择需从运行窗口实际选择/取消。包体、冷启动与多进程开销需在产品构建重测。

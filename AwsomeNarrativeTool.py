import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ==========================================
# 0. 全局语言管理与翻译字典
# ==========================================
GLOBAL_LANG = "CN"

EN_DICT = {
    # 全局及UI文字
    "故事线蓝图编辑器": "Storyline Blueprint Editor",
    "新建故事线": "New Storyline",
    "打开故事线文件": "Open Storyline File",
    "重命名故事线": "Rename Storyline",
    "另存为故事线": "Save Storyline As",
    "导出为表格": "Export to Table",
    "删除故事线": "Delete Storyline",
    "伍冠宇出品 必属精品": "Produced by Wu Guanyu, Quality Assured",
    " (最近打开)": " (Recently Opened)",
    "▶ 开始运行": "▶ Run",
    "■ 结束运行": "■ Stop",
    "回到故事开始": "Back to Start",
    "保存故事线": "Save Storyline",
    "⬅ 返回故事列表": "⬅ Back to List",
    "运行模式:": "Run Mode:",
    "自动运行": "Auto Run",
    "手动运行": "Manual Run",
    "演出实时预览栏：": "Real-time Preview:",
    "属性面板": "Property Panel",
    
    # 导出表格相关
    "导出表格": "Export Table",
    "场次号_对话ID": "Scene_DialogueID",
    "类型": "Type",
    "说话人": "Speaker",
    "情绪": "Emotion",
    "景别": "Shot",
    "场景描述": "Scene Description",
    "对话台本": "Dialogue Script",
    "#注释": "#Note",
    "是否有转场": "Has Transition",
    "播放时长": "Duration",
    "单对话": "Single Dialogue",
    "选项": "Option",
    "场景提示": "Scene Prompt",
    "转场": "Transition",
    
    # 节点名称及内置显示文字
    "故事开始": "Start",
    "对话节点": "Dialogue Node",
    "备注节点": "Note Node",
    "对话分支节点": "Branch Node",
    "淡入淡出": "Fade In/Out",
    "场次": "Scene",
    "ID": "ID",
    
    # 属性面板字段名称
    "场次号": "Scene No",
    "对话ID": "Dialogue ID",
    "注释": "Note",
    "注释透明度": "Note Opacity",
    "备注": "Remark",
    "字体颜色": "Font Color",
    "场景提示台本": "Scene Prompt Script",
    "是否淡入淡出": "Fade In/Out",
    "添加分支 (+)": "Add Branch (+)",
    "选项文本": "Option Text",
    "选项注释": "Option Note",
    "是": "Yes",
    "否": "No",
    
    # 弹窗提示相关
    "提示": "Tip",
    "当前故事线为空或无节点数据！": "Current storyline is empty or has no node data!",
    "警告": "Warning",
    "未找到故事开始节点，无法确定导出顺序！\n将跳过导出，直接保存为空表。": "Cannot find 'Start' node, unable to determine export order!\nWill skip export and save as empty table.",
    "保存成功": "Saved Successfully",
    "错误": "Error",
    "表格已导出到:\n": "Table successfully exported to:\n",
    "导出CSV失败: ": "Failed to export CSV: ",
    "导出XLSX失败: ": "Failed to export XLSX: ",
    "缺少 pandas 或 openpyxl 库，无法导出为 xlsx。\n请尝试导出为 csv 格式，或者通过命令行安装依赖：\n pip install pandas openpyxl": "Missing pandas or openpyxl library, cannot export to xlsx.\nPlease try exporting to csv format, or install via pip:\npip install pandas openpyxl",
    "只能有一个'故事开始'节点！": "Only one 'Start' node is allowed!",
    "回环错误": "Cycle Error",
    "连线将导致逻辑回环，操作被拒绝！": "Connecting will cause a logic cycle, operation rejected!",
    "复制 (Ctrl+C)": "Copy (Ctrl+C)",
    "剪切 (Ctrl+X)": "Cut (Ctrl+X)",
    "粘贴 (Ctrl+V)": "Paste (Ctrl+V)",
    "删除 (Delete)": "Delete (Delete)",
    "切换断点 (Ctrl+T)": "Toggle Breakpoint (Ctrl+T)",
    "删除连接线": "Delete Edge",
    "新建 '故事开始' 节点": "New 'Start' Node",
    "新建 '对话节点'": "New 'Dialogue' Node",
    "新建 '备注节点'": "New 'Note' Node",
    "新建 '对话分支节点'": "New 'Branch' Node",
    "新建 '场景提示' 节点": "New 'Scene Prompt' Node",
    "新建 '转场' 节点": "New 'Transition' Node",
    "未保存提示": "Unsaved Alert",
    "故事线尚未保存，请选择操作：": "Storyline is not saved, please select an action:",
    "保存并返回": "Save & Return",
    "不保存退出": "Discard & Exit",
    "取消": "Cancel",
    "故事线尚未保存，是否保存后退出？": "Storyline is not saved, save and exit?",
    "保存并退出": "Save & Exit",
    "取消退出": "Cancel Exit",
    "确定要删除故事线": "Are you sure you want to delete storyline",
    "吗？\n此操作不可恢复！": "?\nThis operation cannot be undone!",
    "确认删除": "Confirm Delete",
    "名称已存在！": "Name already exists!",
    "新建": "New",
    "输入故事线名称:": "Enter storyline name:",
    "打开文件失败:": "Failed to open file:",
    "重命名": "Rename",
    "输入新的故事线名称:": "Enter new storyline name:",
    "存在场次号和对话ID完全一致的节点！\n重复的节点已被标红高亮显示。": "Nodes with exact Scene No and Dialogue ID exist!\nDuplicates have been highlighted in red.",
    "报错提示": "Error Alert",
    "运行报错": "Run Error",
    "运行时校验失败，存在问题:\n": "Runtime validation failed, issues exist:\n",
    "\n\n请修改红色高亮的节点。": "\n\nPlease modify highlighted nodes.",
    "\n... (更多错误未显示)": "\n... (more errors not shown)",
    "场次号为空": "Scene No is empty",
    "对话ID为空": "Dialogue ID is empty",
    "对话台本为空": "Dialogue Script is empty",
    "播放时长为空": "Duration is empty",
    "播放时长为0": "Duration is 0",
    "播放时长无效": "Duration is invalid",
    "对话节点(参数:": "Dialogue Node(Args:",
    "选项名称为默认值": "Option name is default",
    "对话分支节点(参数:": "Branch Node(Args:",
    "未找到'故事开始'节点！": "Start node not found!",
    "[故事结束]": "[Story End]",
    "[淡出完毕]": "[Fade Out Completed]",
    "[场景提示]": "[Scene Prompt]",
    "[淡入]": "[Fade In]",
    "转场到": "Transitions to",
    "[直接转场]": "[Direct Transition]",
    "[触发断点，暂停运行。请切换到手动运行或重新开始]": "[Breakpoint triggered, running paused. Switch to manual run or restart]",
    "-> 选择了分支:": "-> Selected Branch:",
    "[等待点击继续...]": "[Waiting for click to continue...]",
    "导出失败: ": "Export Failed: ",
    "故事线已导出到:\n": "Storyline exported to:\n",
    "编辑中 - ": "Editing - "
}

def TR(text):
    if GLOBAL_LANG == "EN":
        return EN_DICT.get(text, text)
    return text

# ==========================================
# 辅助工具函数：将故事线导出为表格结构
# ==========================================
def export_to_table(parent_widget, state, default_name=""):
    file_path, _ = QFileDialog.getSaveFileName(parent_widget, TR("导出表格"), default_name, "Excel Files (*.xlsx);;CSV Files (*.csv)")
    if not file_path:
        return
    
    if not state or not state.get("nodes"):
        QMessageBox.warning(parent_widget, TR("提示"), TR("当前故事线为空或无节点数据！"))
        return
        
    nodes = state["nodes"]
    edges = state["edges"]
    
    adj = {i: [] for i in range(len(nodes))}
    edges_by_out = {}
    for e in edges:
        out_node = e["out_node"]
        if out_node not in edges_by_out:
            edges_by_out[out_node] = []
        edges_by_out[out_node].append(e)
    
    for out_node, es in edges_by_out.items():
        es.sort(key=lambda x: x["out_port"])
        for e in es:
            if out_node in adj:
                adj[out_node].append(e["in_node"])
            
    start_nodes = [i for i, n in enumerate(nodes) if n["type"] == "Start"]
    visited = set()
    rows = []
    
    # 动态表头（支持中英文）
    fieldnames = [TR("场次号_对话ID"), TR("类型"), TR("说话人"), TR("情绪"), TR("景别"), TR("场景描述"), TR("对话台本"), TR("#注释"), TR("是否有转场"), TR("播放时长")]
    
    def dfs(curr_idx):
        if curr_idx in visited or curr_idx >= len(nodes):
            return
        visited.add(curr_idx)
        node = nodes[curr_idx]
        n_type = node["type"]
        data = node["data"]
        
        if n_type == "Dialogue":
            row = {f: "" for f in fieldnames}
            row[TR("类型")] = TR("单对话")
            scene = str(data.get('场次号', '')).strip()
            did = str(data.get('对话ID', '')).strip()
            row[TR("场次号_对话ID")] = f"{scene}_{did}" if scene and did else (scene or did)
            row[TR("说话人")] = data.get('说话人', '')
            row[TR("情绪")] = data.get('情绪', '')
            row[TR("景别")] = data.get('景别', '')
            row[TR("场景描述")] = data.get('场景描述', '')
            row[TR("对话台本")] = data.get('对话台本', '')
            row[TR("#注释")] = data.get('注释', '')
            row[TR("播放时长")] = data.get('播放时长', '')
            rows.append(row)
            
        elif n_type == "Branch":
            for opt in data.get("options", []):
                row = {f: "" for f in fieldnames}
                row[TR("类型")] = TR("选项")
                opt_dict = opt if isinstance(opt, dict) else {"text": str(opt), "场次号": "", "对话ID": "", "注释": ""}
                scene = str(opt_dict.get('场次号', '')).strip()
                did = str(opt_dict.get('对话ID', '')).strip()
                row[TR("场次号_对话ID")] = f"{scene}_{did}" if scene and did else (scene or did)
                row[TR("对话台本")] = opt_dict.get('text', '')
                row[TR("#注释")] = opt_dict.get('注释', '')
                rows.append(row)
                
        elif n_type == "ScenePrompt":
            row = {f: "" for f in fieldnames}
            row[TR("类型")] = TR("场景提示")
            row[TR("场次号_对话ID")] = data.get('场景提示台本', '')
            row[TR("播放时长")] = data.get('播放时长', '')
            rows.append(row)
            
        elif n_type == "Transition":
            row = {f: "" for f in fieldnames}
            row[TR("类型")] = TR("转场")
            row[TR("是否有转场")] = "1" if data.get('是否淡入淡出') == '是' else "0"
            row[TR("播放时长")] = data.get('播放时长', '')
            rows.append(row)
            
        for nxt in adj.get(curr_idx, []):
            dfs(nxt)

    if start_nodes:
        dfs(start_nodes[0])
    else:
        QMessageBox.warning(parent_widget, TR("警告"), TR("未找到故事开始节点，无法确定导出顺序！\n将跳过导出，直接保存为空表。"))
    
    if file_path.endswith('.csv'):
        import csv
        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            QMessageBox.information(parent_widget, TR("成功"), TR("表格已导出到:\n") + file_path)
        except Exception as e:
            QMessageBox.critical(parent_widget, TR("错误"), TR("导出CSV失败: ") + str(e))
    elif file_path.endswith('.xlsx'):
        try:
            import pandas as pd
            df = pd.DataFrame(rows, columns=fieldnames)
            df.to_excel(file_path, index=False)
            QMessageBox.information(parent_widget, TR("成功"), TR("表格已导出到:\n") + file_path)
        except ImportError:
            QMessageBox.critical(parent_widget, TR("错误"), TR("缺少 pandas 或 openpyxl 库，无法导出为 xlsx。\n请尝试导出为 csv 格式，或者通过命令行安装依赖：\n pip install pandas openpyxl"))
        except Exception as e:
            QMessageBox.critical(parent_widget, TR("错误"), TR("导出XLSX失败: ") + str(e))

def filter_export_state(state):
    if not state or not state.get("nodes"): return state
    nodes, edges = state["nodes"], state["edges"]
    has_input = set(e["in_node"] for e in edges)
    
    valid_node_indices = [idx for idx, n in enumerate(nodes) if n["type"] == "Start" or idx in has_input]
    if len(valid_node_indices) == len(nodes): return state
        
    new_state = {"nodes": [], "edges": []}
    old_to_new = {}
    for new_idx, old_idx in enumerate(valid_node_indices):
        new_state["nodes"].append(nodes[old_idx])
        old_to_new[old_idx] = new_idx
        
    for e in edges:
        if e["out_node"] in old_to_new and e["in_node"] in old_to_new:
            new_e = dict(e)
            new_e["out_node"] = old_to_new[e["out_node"]]
            new_e["in_node"] = old_to_new[e["in_node"]]
            new_state["edges"].append(new_e)
    return new_state


# ==========================================
# 1. 图形化节点引擎基础模块
# ==========================================

class Port(QGraphicsItem):
    def __init__(self, node, is_output=False, port_id=0):
        super().__init__(node)
        self.node = node
        self.is_output = is_output
        self.port_id = port_id
        self.radius = 6
        self.edges = []
        self.setAcceptHoverEvents(True)

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, 2*self.radius, 2*self.radius)

    def paint(self, painter, option, widget):
        color = QColor(41, 182, 246) if self.edges else QColor(180, 180, 180)
        painter.setBrush(color)
        painter.setPen(QPen(QColor(30, 30, 30), 1.5))
        painter.drawEllipse(self.boundingRect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.is_output:
            self.scene().start_drag(self, event.scenePos())

class Edge(QGraphicsPathItem):
    def __init__(self, port_out, port_in):
        super().__init__()
        self.port_out = port_out
        self.port_in = port_in
        self.setPen(QPen(QColor(150, 150, 150), 2.5))
        self.setZValue(-1)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.update_path()

    def update_path(self):
        start = self.port_out.scenePos()
        end = self.port_in.scenePos()
        path = QPainterPath(start)
        dx = max(60.0, abs(end.x() - start.x()) * 0.5)
        path.cubicTo(start.x() + dx, start.y(), end.x() - dx, end.y(), end.x(), end.y())
        self.setPath(path)

    def shape(self):
        s = QPainterPathStroker()
        s.setWidth(12)
        return s.createStroke(self.path())

    def paint(self, painter, option, widget):
        pen = self.pen()
        if self.isSelected():
            pen.setColor(QColor(0, 122, 204))
            pen.setWidthF(3.5)
        painter.setPen(pen)
        painter.drawPath(self.path())

    def mousePressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier and event.button() == Qt.LeftButton:
            scene = self.scene()
            if scene:
                scene.remove_edge(self)
                scene.save_history() 
            event.accept()
        else:
            super().mousePressEvent(event)

class Node(QGraphicsItem):
    def __init__(self, node_type, scene):
        super().__init__()
        self.node_type = node_type
        self.scene_ref = scene
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.width = 160
        self.height = 90
        self.inputs = []
        self.outputs = []
        self.is_breakpoint = False
        self.is_highlighted = False
        self.is_duplicate_error = False
        self.data = {}
        self.init_node()

    def init_node(self):
        if self.node_type == "Start":
            self.title = "故事开始"
            self.bg_color = QColor(46, 125, 50) 
            self.add_port(is_output=True)
            self.data = {"播放时长": "1"}
        elif self.node_type == "Dialogue":
            self.title = "对话节点"
            self.bg_color = QColor(21, 101, 192)
            self.height = 110
            self.add_port(is_output=False)
            self.add_port(is_output=True)
            self.data = {"场次号": "A1", "对话ID": "001", "说话人": "主角", "情绪": "平静", "景别": "中景", 
                         "场景描述": "白天", "对话台本": "你好！", "注释": "", "注释透明度": 80, "播放时长": "1"}
        elif self.node_type == "Note":
            self.title = "备注节点"
            self.bg_color = QColor(245, 127, 23)
            self.add_port(is_output=False)
            self.add_port(is_output=True)
            self.data = {"备注": "这里是备注", "字体颜色": "Gray", "播放时长": "0"}
        elif self.node_type == "Branch":
            self.title = "对话分支节点"
            self.bg_color = QColor(106, 27, 154)
            self.add_port(is_output=False)
            self.data = {"options": [{"text": "选项1", "场次号": "", "对话ID": "", "注释": ""}, 
                                     {"text": "选项2", "场次号": "", "对话ID": "", "注释": ""}]}
            self.sync_branch_ports()
        elif self.node_type == "ScenePrompt":
            self.title = "场景提示"
            self.bg_color = QColor(239, 108, 0)
            self.add_port(is_output=False)
            self.add_port(is_output=True)
            self.data = {"场景提示台本": "在这里输入场景提示内容...", "播放时长": "1"}
        elif self.node_type == "Transition":
            self.title = "转场"
            self.bg_color = QColor(69, 39, 160)
            self.add_port(is_output=False)
            self.add_port(is_output=True)
            self.data = {"是否淡入淡出": "是", "播放时长": "1"}

    def add_port(self, is_output):
        port_list = self.outputs if is_output else self.inputs
        port = Port(self, is_output, len(port_list))
        port_list.append(port)
        self.update_ports_layout()

    def sync_branch_ports(self):
        while len(self.outputs) > len(self.data["options"]):
            p = self.outputs.pop()
            self.scene_ref.remove_port_edges(p)
            self.scene_ref.removeItem(p)
        while len(self.outputs) < len(self.data["options"]):
            self.add_port(is_output=True)
        self.update_ports_layout()

    def update_ports_layout(self):
        self.height = max(self.height, 40 + max(len(self.inputs), len(self.outputs)) * 20)
        for i, p in enumerate(self.inputs):
            p.setPos(0, 40 + i * 20)
        for i, p in enumerate(self.outputs):
            p.setPos(self.width, 40 + i * 20)
        self.update()

    def boundingRect(self):
        if self.node_type == "Dialogue" and self.data.get("注释", "").strip():
            return QRectF(-5, -50, self.width + 10, self.height + 55)
        return QRectF(-5, -5, self.width + 10, self.height + 10)

    def paint(self, painter, option, widget):
        rect = QRectF(0, 0, self.width, self.height)
        
        painter.setBrush(QColor(0, 0, 0, 60))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect.translated(3, 3), 6, 6)
        
        if self.node_type == "Dialogue" and self.data.get("注释", "").strip():
            note_text = self.data["注释"]
            opacity = min(max(int(self.data.get("注释透明度", 100)), 0), 100) / 100.0
            painter.setOpacity(opacity)
            painter.setBrush(QColor(255, 250, 205))
            painter.setPen(QPen(QColor(50, 50, 50), 1))
            bubble_rect = QRectF(10, -45, self.width - 20, 35)
            painter.drawRoundedRect(bubble_rect, 6, 6)
            
            path = QPainterPath()
            path.moveTo(self.width / 2 - 5, -10)
            path.lineTo(self.width / 2 + 5, -10)
            path.lineTo(self.width / 2, 0)
            painter.drawPath(path)
            
            painter.setPen(QColor(30, 30, 30))
            display_note = note_text[:8] + ("..." if len(note_text) > 8 else "")
            painter.drawText(bubble_rect, Qt.AlignCenter, display_note)
            painter.setOpacity(1.0)

        painter.setBrush(self.bg_color)
        pen_color = QColor(255, 255, 255, 60)
        pen_width = 1.5
        
        if getattr(self, 'is_duplicate_error', False): 
            pen_color = QColor(255, 82, 82)
            pen_width = 3
        elif self.is_highlighted: 
            pen_color = QColor(0, 229, 255)
            pen_width = 3
        elif self.is_breakpoint: 
            pen_color = QColor(255, 82, 82)
            pen_width = 3
        elif self.isSelected(): 
            pen_color = QColor(255, 215, 0)
            pen_width = 2.5
            
        painter.setPen(QPen(pen_color, pen_width))
        painter.drawRoundedRect(rect, 6, 6)

        painter.setBrush(QColor(0, 0, 0, 80))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self.width, 26, 6, 6)
        painter.drawRect(0, 20, self.width, 6) 
        
        painter.setPen(Qt.white)
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(QRectF(0, 0, self.width, 26), Qt.AlignCenter, TR(self.title))
        
        font.setBold(False)
        font.setPointSize(9)
        painter.setFont(font)
        
        if self.node_type == "Dialogue":
            scene = self.data.get("场次号", "")
            d_id = self.data.get("对话ID", "")
            speaker = self.data.get("说话人", "") 
            emotion = self.data.get("情绪", "")
            text = self.data.get("对话台本", "")[:7]
            painter.drawText(QRectF(8, 32, self.width-16, 80), Qt.AlignTop | Qt.AlignLeft, 
                             f"{TR('场次')}: {scene} | {TR('ID')}: {d_id}\n[{speaker}]({emotion}): {text}")
        elif self.node_type == "Transition":
            painter.drawText(QRectF(8, 32, self.width-16, 50), Qt.AlignCenter, 
                             f"{TR('淡入淡出')}: {TR(self.data.get('是否淡入淡出', '是'))}")
        elif self.node_type == "Note":
            text = self.data.get("备注", "")
            display_text = text[:10] + ("..." if len(text) > 10 else "")
            painter.drawText(QRectF(8, 32, self.width-16, 50), Qt.AlignCenter, display_text)
        elif self.node_type == "ScenePrompt":
            text = self.data.get("场景提示台本", "")
            display_text = text[:10] + ("..." if len(text) > 10 else "")
            painter.drawText(QRectF(8, 32, self.width-16, 50), Qt.AlignCenter, display_text)
        elif self.node_type == "Branch":
            for i, opt in enumerate(self.data.get("options", [])):
                opt_dict = opt if isinstance(opt, dict) else {"text": str(opt), "场次号": "", "对话ID": ""}
                text = opt_dict.get("text", "")
                display_opt = text[:5] + ("..." if len(text) > 5 else "")
                y = 40 + i * 20
                painter.drawText(QRectF(5, y - 10, self.width - 20, 20), Qt.AlignRight | Qt.AlignVCenter, display_opt)

        if self.is_breakpoint:
            painter.setBrush(QColor(255, 82, 82))
            painter.setPen(QPen(Qt.white, 1.5))
            painter.drawEllipse(self.width - 16, -8, 14, 14)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for p in self.inputs + self.outputs:
                for edge in p.edges:
                    edge.update_path()
        return super().itemChange(change, value)

class NodeScene(QGraphicsScene):
    dirty_changed = pyqtSignal(bool) 

    def __init__(self, parent=None):
        super().__init__(parent)
        self.nodes = []
        self.edges = []
        self.clipboard = None
        self.drag_port = None
        self.temp_edge = None
        self.history = []
        self.is_undoing = False
        self._is_dirty = False

    def set_dirty(self, val=True):
        if self._is_dirty != val:
            self._is_dirty = val
            self.dirty_changed.emit(val)

    def save_history(self):
        if self.is_undoing: return
        state = self.serialize_scene()
        self.history.append(state)
        if len(self.history) > 30: 
            self.history.pop(0)
        self.set_dirty(True)

    def undo(self):
        if len(self.history) > 1:
            self.history.pop() 
            state = self.history[-1]
            self.deserialize_scene(state)
            self.set_dirty(True)
        elif len(self.history) == 1:
            state = self.history[0]
            self.deserialize_scene(state)
            self.set_dirty(True)

    def serialize_scene(self):
        state = {"nodes": [], "edges": []}
        node_to_idx = {node: idx for idx, node in enumerate(self.nodes)}
        for node in self.nodes:
            state["nodes"].append({
                "type": node.node_type,
                "pos": (node.scenePos().x(), node.scenePos().y()),
                "data": json.loads(json.dumps(node.data))
            })
        for edge in self.edges:
            state["edges"].append({
                "out_node": node_to_idx[edge.port_out.node],
                "out_port": edge.port_out.port_id,
                "in_node": node_to_idx[edge.port_in.node],
                "in_port": edge.port_in.port_id
            })
        return state

    def clear_scene_completely(self):
        for edge in self.edges:
            edge.port_out.edges.clear()
            edge.port_in.edges.clear()
        self.edges.clear()
        for node in self.nodes:
            self.removeItem(node)
        self.nodes.clear()
        self.clear()

    def deserialize_scene(self, state):
        self.is_undoing = True
        self.clear_scene_completely()
        
        idx_to_node = {}
        for idx, n_data in enumerate(state.get("nodes", [])):
            node = Node(n_data["type"], self)
            node.setPos(n_data["pos"][0], n_data["pos"][1])
            node.data = json.loads(json.dumps(n_data["data"]))
            if node.node_type == "Branch": 
                opts = node.data.get("options", [])
                for i, opt in enumerate(opts):
                    if isinstance(opt, str):
                        opts[i] = {"text": opt, "场次号": "", "对话ID": "", "注释": ""}
                    elif isinstance(opt, dict) and "注释" not in opt:
                        opt["注释"] = ""
                node.sync_branch_ports()
            self.addItem(node)
            self.nodes.append(node)
            idx_to_node[idx] = node
            
        for e_data in state.get("edges", []):
            out_node = idx_to_node.get(e_data["out_node"])
            in_node = idx_to_node.get(e_data["in_node"])
            if out_node and in_node:
                out_port = out_node.outputs[e_data["out_port"]]
                in_port = in_node.inputs[e_data["in_port"]]
                edge = Edge(out_port, in_port)
                self.addItem(edge)
                self.edges.append(edge)
                out_port.edges.append(edge)
                in_port.edges.append(edge)
                
        self.is_undoing = False
        self.update()
        self.clearSelection() 

    def has_cycle(self, start_node, target_node, depth=0):
        if depth > 500: return True
        visited = set()
        def dfs(node, d):
            if node == start_node: return True
            if d > 500: return True
            visited.add(node)
            for port in node.outputs:
                for edge in port.edges:
                    next_node = edge.port_in.node
                    if next_node not in visited:
                        if dfs(next_node, d + 1): return True
            return False
        return dfs(target_node, depth)

    def add_node(self, node_type, pos):
        if node_type == "Start" and any(n.node_type == "Start" for n in self.nodes):
            QMessageBox.warning(None, TR("警告"), TR("只能有一个'故事开始'节点！"))
            return None
        node = Node(node_type, self)
        node.setPos(pos)
        self.addItem(node)
        self.nodes.append(node)
        self.save_history() 
        return node

    def remove_node(self, node):
        for p in node.inputs + node.outputs:
            self.remove_port_edges(p)
        if node in self.nodes:
            self.nodes.remove(node)
        self.removeItem(node)

    def remove_edge(self, edge):
        if edge in self.edges: self.edges.remove(edge)
        if edge in edge.port_out.edges: edge.port_out.edges.remove(edge)
        if edge in edge.port_in.edges: edge.port_in.edges.remove(edge)
        self.removeItem(edge)

    def remove_port_edges(self, port):
        for e in list(port.edges):
            self.remove_edge(e)

    def start_drag(self, port, pos):
        self.drag_port = port
        self.temp_edge = QGraphicsPathItem()
        self.temp_edge.setPen(QPen(QColor(41, 182, 246), 2, Qt.DashLine))
        self.addItem(self.temp_edge)
        self.update_temp_edge(pos)

    def update_temp_edge(self, pos):
        if self.drag_port and self.temp_edge:
            start = self.drag_port.scenePos()
            path = QPainterPath(start)
            dx = max(60.0, abs(pos.x() - start.x()) * 0.5)
            path.cubicTo(start.x() + dx, start.y(), pos.x() - dx, pos.y(), pos.x(), pos.y())
            self.temp_edge.setPath(path)

    def mouseMoveEvent(self, event):
        if self.drag_port:
            self.update_temp_edge(event.scenePos())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.drag_port:
            items = self.items(event.scenePos())
            for item in items:
                if isinstance(item, Port) and not item.is_output and item.node != self.drag_port.node:
                    if self.has_cycle(self.drag_port.node, item.node):
                        QMessageBox.warning(None, TR("回环错误"), TR("连线将导致逻辑回环，操作被拒绝！"))
                        break
                    self.remove_port_edges(item) 
                    edge = Edge(self.drag_port, item)
                    self.addItem(edge)
                    self.edges.append(edge)
                    self.drag_port.edges.append(edge)
                    item.edges.append(edge)
                    self.save_history()
                    break
            if self.temp_edge:
                self.removeItem(self.temp_edge)
            self.drag_port = None
            self.temp_edge = None
        else:
            super().mouseReleaseEvent(event)
            if event.button() == Qt.LeftButton and self.selectedItems():
                if self.history:
                    curr_state = self.serialize_scene()
                    if curr_state != self.history[-1]:
                        self.save_history()


# ==========================================
# 2. 画布视图与属性面板
# ==========================================

class StoryView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setSceneRect(-1000000, -1000000, 2000000, 2000000)
        self.setFrameShape(QFrame.NoFrame)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        left = int(rect.left()) - (int(rect.left()) % 25)
        top = int(rect.top()) - (int(rect.top()) % 25)
        lines = []
        for x in range(left, int(rect.right()), 25):
            lines.append(QLineF(x, rect.top(), x, rect.bottom()))
        for y in range(top, int(rect.bottom()), 25):
            lines.append(QLineF(rect.left(), y, rect.right(), y))
        painter.setPen(QPen(QColor(45, 45, 45), 1))
        painter.drawLines(lines)

    def mousePressEvent(self, event):
        if event.button() == Qt.MidButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            fake_event = QMouseEvent(event.type(), event.localPos(), event.windowPos(), event.screenPos(),
                                     Qt.LeftButton, Qt.LeftButton, event.modifiers())
            super().mousePressEvent(fake_event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MidButton:
            fake_event = QMouseEvent(event.type(), event.localPos(), event.windowPos(), event.screenPos(),
                                     Qt.LeftButton, Qt.NoButton, event.modifiers())
            super().mouseReleaseEvent(fake_event)
            self.setDragMode(QGraphicsView.RubberBandDrag)
        else:
            super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)


class ClickableTextBrowser(QTextBrowser):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class PropertyPanel(QWidget):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.current_node = None
        self.setFixedWidth(320)
        self.setObjectName("PropertyPanel")
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        
        self.content_widget = QWidget()
        self.content_widget.setObjectName("PropertyContentWidget")
        self.layout = QVBoxLayout(self.content_widget)
        
        self.title_label = QLabel(TR("属性面板"))
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 8px;")
        self.layout.addWidget(self.title_label)
        
        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(12)
        self.layout.addLayout(self.form_layout)
        self.layout.addStretch()
        
        self.scroll_area.setWidget(self.content_widget)
        main_layout.addWidget(self.scroll_area)

    def update_ui_text(self):
        self.title_label.setText(TR("属性面板"))
        self.update_panel()

    def update_panel(self):
        while self.form_layout.count():
            item = self.form_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        selected = self.scene.selectedItems()
        if not selected or not isinstance(selected[0], Node):
            self.current_node = None
            return
        
        self.current_node = selected[0]
        node = self.current_node

        for key, val in node.data.items():
            if key == "options": 
                self.build_branch_ui(node)
                continue
                
            if key == "是否淡入淡出":
                cb = QComboBox()
                cb.addItems([TR("是"), TR("否")])
                cb.setCurrentText(TR(str(val)))
                cb.currentTextChanged.connect(lambda text, k=key: self.save_data(k, "是" if text==TR("是") else "否"))
                self.form_layout.addRow(TR(key), cb)
                
            elif key == "注释透明度":
                slider = QSlider(Qt.Horizontal)
                slider.setRange(0, 100)
                slider.setValue(int(val))
                slider.valueChanged.connect(lambda v, k=key: self.save_data(k, v))
                self.form_layout.addRow(TR(key), slider)
                
            elif key in ["对话台本", "注释", "场景描述", "备注", "场景提示台本"]:
                edit = QTextEdit()
                edit.setFixedHeight(75)
                edit.setText(str(val))
                edit.textChanged.connect(lambda k=key, w=edit: self.save_data(k, w.toPlainText()))
                self.form_layout.addRow(TR(key), edit)
                
            else: 
                edit = QLineEdit()
                edit.setText(str(val))
                edit.textChanged.connect(lambda text, k=key: self.save_data(k, text))
                self.form_layout.addRow(TR(key), edit)

    def save_data(self, key, value):
        if self.current_node:
            self.current_node.data[key] = value
            self.current_node.update()
            self.scene.set_dirty(True)

    def build_branch_ui(self, node):
        btn_add = QPushButton(TR("添加分支 (+)"))
        btn_add.clicked.connect(self.add_branch)
        self.form_layout.addRow(btn_add)
        for i, opt in enumerate(node.data["options"]):
            if isinstance(opt, str):
                opt = {"text": opt, "场次号": "", "对话ID": "", "注释": ""}
                node.data["options"][i] = opt
            
            v_layout = QVBoxLayout()
            v_layout.setContentsMargins(0, 0, 0, 5)
            v_layout.setSpacing(6)
            
            edit_text = QLineEdit(opt.get("text", ""))
            edit_text.setPlaceholderText(TR("选项文本"))
            edit_text.textChanged.connect(lambda text, idx=i: self.update_branch_dict(idx, "text", text))
            
            h_layout = QHBoxLayout()
            edit_scene = QLineEdit(opt.get("场次号", ""))
            edit_scene.setPlaceholderText(TR("场次号"))
            edit_scene.textChanged.connect(lambda text, idx=i: self.update_branch_dict(idx, "场次号", text))
            
            edit_id = QLineEdit(opt.get("对话ID", ""))
            edit_id.setPlaceholderText(TR("对话ID"))
            edit_id.textChanged.connect(lambda text, idx=i: self.update_branch_dict(idx, "对话ID", text))
            
            h_layout.addWidget(edit_scene)
            h_layout.addWidget(edit_id)
            
            h_layout_note = QHBoxLayout()
            edit_note = QLineEdit(opt.get("注释", ""))
            edit_note.setPlaceholderText(TR("选项注释"))
            edit_note.textChanged.connect(lambda text, idx=i: self.update_branch_dict(idx, "注释", text))
            h_layout_note.addWidget(edit_note)
            
            v_layout.addWidget(edit_text)
            v_layout.addLayout(h_layout)
            v_layout.addLayout(h_layout_note)
            
            container = QWidget()
            container.setObjectName("PropertyBranchContainer")
            container.setLayout(v_layout)
            self.form_layout.addRow(f"{TR('选项')} {i+1}", container)

    def add_branch(self):
        if self.current_node:
            idx = len(self.current_node.data['options']) + 1
            self.current_node.data["options"].append({"text": f"新选项 {idx}", "场次号": "", "对话ID": "", "注释": ""})
            self.current_node.sync_branch_ports()
            self.scene.set_dirty(True)
            self.update_panel()

    def update_branch_dict(self, idx, key, val):
        if self.current_node:
            opt = self.current_node.data["options"][idx]
            if isinstance(opt, dict):
                opt[key] = val
            self.current_node.update()
            self.scene.set_dirty(True)


# ==========================================
# 3. 故事线大纲视图 (主UI及引擎)
# ==========================================

class StoryOutlineWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setObjectName("StoryOutlineWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        
        self.toolbar = QHBoxLayout()
        self.title_label = QLabel()
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #4fc3f7;")
        self.title_label.setAlignment(Qt.AlignVCenter)
        
        self.btn_play = QPushButton(TR("▶ 开始运行"))
        self.btn_play.setStyleSheet("background-color: #2e7d32; border-color: #1b5e20;")
        self.btn_stop = QPushButton(TR("■ 结束运行"))
        self.btn_stop.setStyleSheet("background-color: #c62828; border-color: #b71c1c;")
        
        self.run_mode_combo = QComboBox()
        self.run_mode_combo.addItems([TR("自动运行"), TR("手动运行")])
        self.lbl_run_mode = QLabel(TR("运行模式:"))
        
        self.btn_center_start = QPushButton(TR("回到故事开始"))
        self.btn_save_outline = QPushButton(TR("保存故事线"))
        self.btn_export = QPushButton(TR("另存为故事线")) 
        self.btn_export_table = QPushButton(TR("导出为表格")) 
        self.btn_back = QPushButton(TR("⬅ 返回故事列表"))
        
        self.toolbar.addWidget(self.title_label)
        self.toolbar.addStretch()
        self.toolbar.addWidget(self.lbl_run_mode)
        self.toolbar.addWidget(self.run_mode_combo)
        self.toolbar.addWidget(self.btn_play)
        self.toolbar.addWidget(self.btn_stop)
        self.toolbar.addWidget(self.btn_center_start)
        self.toolbar.addWidget(self.btn_save_outline)
        self.toolbar.addWidget(self.btn_export)
        self.toolbar.addWidget(self.btn_export_table)
        self.toolbar.addWidget(self.btn_back)
        self.layout.addLayout(self.toolbar)

        self.h_layout = QHBoxLayout()
        self.scene = NodeScene()
        self.scene.selectionChanged.connect(self.on_selection_changed)
        self.scene.dirty_changed.connect(self.update_title)
        
        self.view = StoryView(self.scene)
        self.view.customContextMenuRequested.connect(self.show_context_menu)
        
        self.perf_panel = ClickableTextBrowser()
        self.perf_panel.setFixedHeight(180)
        self.perf_panel.setStyleSheet("background-color: #1e1e1e; font-size: 14px; border: 1px solid #3e3e42;")
        self.perf_panel.clicked.connect(self.manual_step)
        
        self.branch_widget = QWidget()
        self.branch_widget.setObjectName("BranchWidget")
        self.branch_layout = QVBoxLayout(self.branch_widget)
        self.branch_widget.hide()

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.view)
        
        self.perf_label = QLabel(TR("演出实时预览栏："))
        self.perf_label.setStyleSheet("font-weight: bold; color: #a0a0a0; margin-top: 10px;")
        left_layout.addWidget(self.perf_label)
        left_layout.addWidget(self.perf_panel)
        left_layout.addWidget(self.branch_widget)
        
        self.prop_panel = PropertyPanel(self.scene)
        
        self.h_layout.addLayout(left_layout, 7)
        self.h_layout.addWidget(self.prop_panel, 3)
        self.layout.addLayout(self.h_layout)

        self.run_timer = QTimer()
        self.run_timer.timeout.connect(self.step_execution)
        self.current_exec_node = None
        self.is_running = False
        self.pending_fade_out = False

        self.btn_play.clicked.connect(self.play_logic)
        self.btn_stop.clicked.connect(self.stop_logic)
        self.btn_center_start.clicked.connect(self.center_to_start)
        self.btn_save_outline.clicked.connect(self.save_story)
        self.btn_export.clicked.connect(self.export_story)
        self.btn_export_table.clicked.connect(self.export_table_action)
        self.btn_back.clicked.connect(self.on_back_clicked)

    def update_ui_text(self):
        self.btn_play.setText(TR("▶ 开始运行"))
        self.btn_stop.setText(TR("■ 结束运行"))
        self.run_mode_combo.setItemText(0, TR("自动运行"))
        self.run_mode_combo.setItemText(1, TR("手动运行"))
        self.lbl_run_mode.setText(TR("运行模式:"))
        self.btn_center_start.setText(TR("回到故事开始"))
        self.btn_save_outline.setText(TR("保存故事线"))
        self.btn_export.setText(TR("另存为故事线"))
        self.btn_export_table.setText(TR("导出为表格"))
        self.btn_back.setText(TR("⬅ 返回故事列表"))
        self.perf_label.setText(TR("演出实时预览栏："))
        self.update_title()
        self.prop_panel.update_ui_text()
        self.scene.update()

    def update_title(self):
        name = self.main_window.current_story_name
        if not name: return
        if self.scene._is_dirty:
            self.title_label.setText(f"<i>*{name}*</i>")
            self.main_window.setWindowTitle(TR("编辑中 - ") + f"*{name}")
        else:
            self.title_label.setText(f"{name}")
            self.main_window.setWindowTitle(TR("编辑中 - ") + f"{name}")

    def on_back_clicked(self):
        if self.scene._is_dirty:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle(TR("未保存提示"))
            msg_box.setText(TR("故事线尚未保存，请选择操作："))
            btn_save = msg_box.addButton(TR("保存并返回"), QMessageBox.AcceptRole)
            btn_discard = msg_box.addButton(TR("不保存退出"), QMessageBox.DestructiveRole)
            btn_cancel = msg_box.addButton(TR("取消"), QMessageBox.RejectRole)
            msg_box.exec_()
            
            if msg_box.clickedButton() == btn_save:
                self.save_story()
                self.main_window.stacked.setCurrentIndex(0)
            elif msg_box.clickedButton() == btn_discard:
                self.scene.set_dirty(False)
                self.main_window.stacked.setCurrentIndex(0)
            else:
                return
        else:
            self.main_window.stacked.setCurrentIndex(0)

    def save_story(self):
        name = self.main_window.current_story_name
        if name:
            state = self.scene.serialize_scene()
            self.main_window.list_widget.stories[name] = state
            self.scene.set_dirty(False)
            QMessageBox.information(self, TR("保存成功"), TR("保存成功"))

    def export_table_action(self):
        self.save_story() 
        state = self.scene.serialize_scene()
        export_to_table(self, state, self.main_window.current_story_name)

    def on_selection_changed(self):
        self.prop_panel.update_panel()
        
    def center_to_start(self):
        for n in self.scene.nodes:
            if n.node_type == "Start":
                self.view.centerOn(n)
                break

    def export_story(self):
        file_path, _ = QFileDialog.getSaveFileName(self, TR("另存为故事线"), "", "JSON Files (*.json);;All Files (*)")
        if file_path:
            try:
                state = self.scene.serialize_scene()
                state = filter_export_state(state)
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(state, f, ensure_ascii=False, indent=4)
                QMessageBox.information(self, TR("成功"), TR("故事线已导出到:\n") + file_path)
            except Exception as e:
                QMessageBox.critical(self, TR("错误"), TR("导出失败: ") + str(e))

    def show_context_menu(self, pos):
        menu = QMenu()
        menu.setStyleSheet("QMenu { background-color: #2d2d30; border: 1px solid #3e3e42; } QMenu::item:selected { background-color: #094771; }")
        scene_pos = self.view.mapToScene(pos)
        item = self.scene.itemAt(scene_pos, QTransform())
        
        if isinstance(item, Node):
            self.scene.clearSelection()
            item.setSelected(True)
            menu.addAction(TR("复制 (Ctrl+C)"), self.copy_node)
            menu.addAction(TR("剪切 (Ctrl+X)"), self.cut_node)
            menu.addAction(TR("粘贴 (Ctrl+V)"), lambda: self.paste_node(scene_pos))
            menu.addAction(TR("删除 (Delete)"), self.delete_node)
            menu.addAction(TR("切换断点 (Ctrl+T)"), self.toggle_breakpoint)
        elif isinstance(item, Edge):
            self.scene.clearSelection()
            item.setSelected(True)
            menu.addAction(TR("删除连接线"), self.delete_node)
        else:
            menu.addAction(TR("新建 '故事开始' 节点"), lambda: self.scene.add_node("Start", scene_pos))
            menu.addAction(TR("新建 '对话节点'"), lambda: self.scene.add_node("Dialogue", scene_pos))
            menu.addAction(TR("新建 '备注节点'"), lambda: self.scene.add_node("Note", scene_pos))
            menu.addAction(TR("新建 '对话分支节点'"), lambda: self.scene.add_node("Branch", scene_pos))
            menu.addAction(TR("新建 '场景提示' 节点"), lambda: self.scene.add_node("ScenePrompt", scene_pos))
            menu.addAction(TR("新建 '转场' 节点"), lambda: self.scene.add_node("Transition", scene_pos))
            if self.scene.clipboard:
                menu.addAction(TR("粘贴 (Ctrl+V)"), lambda: self.paste_node(scene_pos))
        menu.exec_(self.view.mapToGlobal(pos))

    def get_selected_node(self):
        items = self.scene.selectedItems()
        return items[0] if items and isinstance(items[0], Node) else None

    def delete_node(self):
        nodes = [item for item in self.scene.selectedItems() if isinstance(item, Node)]
        edges = [item for item in self.scene.selectedItems() if isinstance(item, Edge)]
        if nodes or edges:
            for node in nodes:
                self.scene.remove_node(node)
            for edge in edges:
                self.scene.remove_edge(edge)
            self.scene.save_history()

    def copy_node(self):
        node = self.get_selected_node()
        if node: self.scene.clipboard = {"type": node.node_type, "data": json.dumps(node.data)}

    def cut_node(self):
        self.copy_node()
        self.delete_node()

    def paste_node(self, pos):
        if self.scene.clipboard:
            new_node = self.scene.add_node(self.scene.clipboard["type"], pos)
            if new_node:
                new_node.data = json.loads(self.scene.clipboard["data"])
                if new_node.node_type == "Branch": new_node.sync_branch_ports()
                new_node.update()
                self.scene.save_history()

    def toggle_breakpoint(self):
        node = self.get_selected_node()
        if node:
            node.is_breakpoint = not node.is_breakpoint
            node.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delete_node()
        elif event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_C: self.copy_node()
            elif event.key() == Qt.Key_X: self.cut_node()
            elif event.key() == Qt.Key_V: 
                self.paste_node(self.view.mapToScene(self.view.mapFromGlobal(QCursor.pos())))
            elif event.key() == Qt.Key_T: self.toggle_breakpoint()
            elif event.key() == Qt.Key_D: 
                self.copy_node()
                selected = self.scene.selectedItems()
                if selected and isinstance(selected[0], Node):
                    pos = selected[0].scenePos() + QPointF(20, 20)
                else:
                    pos = self.view.mapToScene(self.view.mapFromGlobal(QCursor.pos()))
                self.paste_node(pos)
                self.scene.save_history()
            elif event.key() == Qt.Key_R: 
                self.scene.undo()
        super().keyPressEvent(event)

    def validate_nodes(self):
        has_error = False
        error_messages = []
        for node in self.scene.nodes:
            node.is_duplicate_error = False
        
        for node in self.scene.nodes:
            if node.node_type == "Dialogue":
                scene = str(node.data.get("场次号", "")).strip()
                d_id = str(node.data.get("对话ID", "")).strip()
                text = str(node.data.get("对话台本", "")).strip()
                duration = str(node.data.get("播放时长", "")).strip()
                
                errors = []
                if not scene: errors.append(TR("场次号为空"))
                if not d_id: errors.append(TR("对话ID为空"))
                if not text: errors.append(TR("对话台本为空"))
                
                if not duration:
                    errors.append(TR("播放时长为空"))
                else:
                    try:
                        if float(duration) == 0.0:
                            errors.append(TR("播放时长为0"))
                    except ValueError:
                        errors.append(TR("播放时长无效"))
                        
                if errors:
                    node.is_duplicate_error = True
                    has_error = True
                    error_messages.append(f"{TR('对话节点(参数:')} {', '.join(errors)})")
                    
            elif node.node_type == "Branch":
                opts = node.data.get("options", [])
                errors = []
                for idx, opt in enumerate(opts):
                    opt_dict = opt if isinstance(opt, dict) else {"text": str(opt)}
                    text = str(opt_dict.get("text", "")).strip()
                    scene = str(opt_dict.get("场次号", "")).strip()
                    d_id = str(opt_dict.get("对话ID", "")).strip()
                    
                    if text.startswith("选项") or text.startswith("新选项") or not text:
                        errors.append(TR("选项名称为默认值"))
                    if not scene: errors.append(TR("场次号为空"))
                    if not d_id: errors.append(TR("对话ID为空"))
                    
                if errors:
                    unique_errors = list(dict.fromkeys(errors))
                    node.is_duplicate_error = True
                    has_error = True
                    error_messages.append(f"{TR('对话分支节点(参数:')} {', '.join(unique_errors)})")

        if has_error:
            err_text = "\n".join(error_messages[:10])
            if len(error_messages) > 10:
                err_text += TR("\n... (更多错误未显示)")
            QMessageBox.critical(self, TR("运行报错"), TR("运行时校验失败，存在问题:\n") + err_text + TR("\n\n请修改红色高亮的节点。"))
            for node in self.scene.nodes:
                node.update()
            return False
            
        return True

    def check_duplicate_ids(self):
        id_map = {}
        duplicates = set()
        for node in self.scene.nodes:
            if not getattr(node, 'is_duplicate_error', False):
                node.is_duplicate_error = False
            items = []
            
            if node.node_type == "Dialogue":
                s_no = node.data.get("场次号", "").strip()
                d_id = node.data.get("对话ID", "").strip()
                if s_no and d_id:
                    items.append((s_no, d_id))
            elif node.node_type == "Branch":
                for opt in node.data.get("options", []):
                    if isinstance(opt, dict):
                        s_no = opt.get("场次号", "").strip()
                        d_id = opt.get("对话ID", "").strip()
                        if s_no and d_id:
                            items.append((s_no, d_id))
            
            for k in items:
                if k in id_map:
                    duplicates.add(id_map[k])
                    duplicates.add(node)
                else:
                    id_map[k] = node
                    
        if duplicates:
            QMessageBox.critical(self, TR("报错提示"), TR("存在场次号和对话ID完全一致的节点！\n重复的节点已被标红高亮显示。"))
            for n in duplicates:
                n.is_duplicate_error = True
                n.update()
            return True
        return False

    def play_logic(self):
        if not self.validate_nodes():
            return
        if self.check_duplicate_ids():
            return
            
        if not self.is_running:
            start_nodes = [n for n in self.scene.nodes if n.node_type == "Start"]
            if not start_nodes:
                QMessageBox.warning(self, TR("错误"), TR("未找到'故事开始'节点！"))
                return
            self.current_exec_node = start_nodes[0]
            self.is_running = True
            self.pending_fade_out = False
            self.perf_panel.clear()
            self.step_execution()

    def stop_logic(self):
        self.run_timer.stop()
        self.is_running = False
        self.current_exec_node = None
        self.pending_fade_out = False
        self.perf_panel.clear()
        self.branch_widget.hide()
        self.perf_panel.show()
        for n in self.scene.nodes:
            n.is_highlighted = False
            n.update()

    def manual_step(self):
        if self.is_running and self.run_mode_combo.currentText() == TR("手动运行"):
            self.step_execution()

    def get_prev_scene(self, node):
        if not node.inputs or not node.inputs[0].edges: return "未知起点"
        prev_node = node.inputs[0].edges[0].port_out.node
        if prev_node.node_type == "Dialogue":
            return prev_node.data.get("场次号", "未知场次")
        return self.get_prev_scene(prev_node)

    def get_next_scene(self, node):
        if not node.outputs or not node.outputs[0].edges: return "未知终点"
        next_node = node.outputs[0].edges[0].port_in.node
        if next_node.node_type == "Dialogue":
            return next_node.data.get("场次号", "未知场次")
        return self.get_next_scene(next_node)

    def step_execution(self):
        if not self.current_exec_node:
            self.stop_logic()
            self.perf_panel.append(f"<font color='#00e676'><b>{TR('[故事结束]')}</b></font>")
            return

        for n in self.scene.nodes: n.is_highlighted = False
        node = self.current_exec_node
        node.is_highlighted = True
        node.update()
        
        self.view.centerOn(node)

        self.perf_panel.show()
        self.branch_widget.hide()

        if self.pending_fade_out:
            self.perf_panel.append(f"<p><font color='#b388ff'><i>{TR('[淡出完毕]')}</i></font></p>")
            self.pending_fade_out = False

        if node.node_type == "Dialogue":
            d = node.data
            html = f"<p><b>[{d.get('景别','')} : {d.get('场景描述','')}]</b> <span style='color:#90caf9'>({d.get('场次号','')}_{d.get('对话ID','')})</span><br>"
            html += f"<span style='color:#ffcc80'>{d.get('说话人','')}</span> ({d.get('情绪','')}): {d.get('对话台本','')}</p>"
            self.perf_panel.append(html)
            
        elif node.node_type == "Note":
            d = node.data
            color = d.get('字体颜色', 'Gray')
            self.perf_panel.append(f"<p><font color='{color}'>{d.get('备注','')}</font></p>")
            
        elif node.node_type == "ScenePrompt":
            self.perf_panel.append(f"<p style='color:#ffb74d;'><b>{TR('[场景提示]')}</b> {node.data.get('场景提示台本','')}</p>")
            
        elif node.node_type == "Transition":
            if node.data.get("是否淡入淡出") == "是":
                prev_scene = self.get_prev_scene(node)
                next_scene = self.get_next_scene(node)
                self.perf_panel.append(f"<p><font color='#b388ff'><i>{TR('[淡入]')}</i></font></p>")
                self.perf_panel.append(f"<p><b>【 {prev_scene} 】 {TR('转场到')} 【 {next_scene} 】</b></p>")
                self.pending_fade_out = True
            else:
                self.perf_panel.append(f"<p><b>{TR('[直接转场]')}</b></p>")

        elif node.node_type == "Branch":
            self.run_timer.stop() 
            self.perf_panel.hide()
            self.branch_widget.show()
            for i in reversed(range(self.branch_layout.count())): 
                self.branch_layout.itemAt(i).widget().setParent(None)
            
            opts = node.data.get("options", [])
            font_size = max(14, 24 - len(opts)*2)
            
            for i, opt in enumerate(opts):
                opt_dict = opt if isinstance(opt, dict) else {"text": str(opt), "场次号": "", "对话ID": ""}
                btn = QPushButton(opt_dict.get("text", ""))
                btn.setStyleSheet(f"font-size: {font_size}px; padding: 12px; background-color: #3f51b5; border:none; border-radius:4px; margin:4px;")
                btn.clicked.connect(lambda checked, idx=i: self.branch_selected(idx))
                self.branch_layout.addWidget(btn)
            return

        if node.is_breakpoint and self.run_mode_combo.currentText() == TR("自动运行"):
            self.run_timer.stop()
            self.perf_panel.append(f"<font color='#ff5252'><b>{TR('[触发断点，暂停运行。请切换到手动运行或重新开始]')}</b></font>")
            return

        self.move_to_next_node(0)

        if self.run_mode_combo.currentText() == TR("自动运行"):
            duration_sec = 1.0
            try:
                duration_sec = float(node.data.get("播放时长", 1.0))
            except ValueError:
                pass
            self.run_timer.start(int(duration_sec * 1000))
        else:
            self.run_timer.stop() 

    def branch_selected(self, index):
        self.branch_widget.hide()
        self.perf_panel.show()
        
        opt = self.current_exec_node.data['options'][index]
        opt_dict = opt if isinstance(opt, dict) else {"text": str(opt)}
        self.perf_panel.append(f"<p><i>{TR('-> 选择了分支:')} {opt_dict.get('text', '')}</i></p>")
        
        self.move_to_next_node(index)
        
        if self.run_mode_combo.currentText() == TR("自动运行"):
            self.step_execution()
        else:
            self.perf_panel.append(f"<p><font color='#888888'><i>{TR('[等待点击继续...]')}</i></font></p>")

    def move_to_next_node(self, port_index):
        if not self.current_exec_node or port_index >= len(self.current_exec_node.outputs):
            self.current_exec_node = None
            return
        
        edges = self.current_exec_node.outputs[port_index].edges
        if edges:
            self.current_exec_node = edges[0].port_in.node
        else:
            self.current_exec_node = None


# ==========================================
# 4. 故事管理视图 (列表UI)
# ==========================================

class StoryListWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setObjectName("StoryListWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self.stories = {"示例故事线": None} 
        self.recent_story_name = None
        
        main_layout = QVBoxLayout(self)
        
        self.title_label = QLabel(TR("故事线蓝图编辑器"))
        self.title_label.setFont(QFont("Microsoft YaHei", 24, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("margin: 20px; color: #4fc3f7;")
        main_layout.addWidget(self.title_label)

        content_layout = QHBoxLayout()
        
        self.list_widget = QListWidget()
        self.list_widget.doubleClicked.connect(self.edit_story)
        self.update_list()
        
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(15)
        
        self.btn_switch_lang = QPushButton("Switch to English" if GLOBAL_LANG == "CN" else "切换为中文")
        self.btn_switch_lang.setStyleSheet("background-color: #6a1b9a; border-color: #4a148c;")
        self.btn_switch_lang.clicked.connect(self.switch_language)
        
        self.btn_new = QPushButton(TR("新建故事线"))
        self.btn_open = QPushButton(TR("打开故事线文件"))
        self.btn_rename = QPushButton(TR("重命名故事线"))
        self.btn_export = QPushButton(TR("另存为故事线"))
        self.btn_export_table = QPushButton(TR("导出为表格"))
        self.btn_delete = QPushButton(TR("删除故事线"))
        self.btn_delete.setStyleSheet("background-color: #c62828; border-color: #b71c1c;")
        
        self.btn_new.clicked.connect(self.new_story)
        self.btn_open.clicked.connect(self.open_story_file)
        self.btn_rename.clicked.connect(self.rename_story)
        self.btn_export.clicked.connect(self.export_story_list)
        self.btn_export_table.clicked.connect(self.export_table_list_action)
        self.btn_delete.clicked.connect(self.delete_story)

        btn_layout.addWidget(self.btn_switch_lang)
        btn_layout.addWidget(self.btn_new)
        btn_layout.addWidget(self.btn_open)
        btn_layout.addWidget(self.btn_rename)
        btn_layout.addWidget(self.btn_export)
        btn_layout.addWidget(self.btn_export_table)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_delete)
        
        content_layout.addWidget(self.list_widget, 7)
        content_layout.addLayout(btn_layout, 2)
        
        main_layout.addLayout(content_layout)
        
        self.watermark_label = QLabel(TR("伍冠宇出品 必属精品"))
        self.watermark_label.setAlignment(Qt.AlignCenter)
        self.watermark_label.setStyleSheet("color: #888888; font-size: 14px; font-weight: bold; margin-top: 10px; margin-bottom: 5px;")
        main_layout.addWidget(self.watermark_label)

    def switch_language(self):
        global GLOBAL_LANG
        if GLOBAL_LANG == "CN":
            GLOBAL_LANG = "EN"
        else:
            GLOBAL_LANG = "CN"
        self.main_window.update_language()

    def update_ui_text(self):
        self.title_label.setText(TR("故事线蓝图编辑器"))
        self.btn_new.setText(TR("新建故事线"))
        self.btn_open.setText(TR("打开故事线文件"))
        self.btn_rename.setText(TR("重命名故事线"))
        self.btn_export.setText(TR("另存为故事线"))
        self.btn_export_table.setText(TR("导出为表格"))
        self.btn_delete.setText(TR("删除故事线"))
        self.watermark_label.setText(TR("伍冠宇出品 必属精品"))
        self.btn_switch_lang.setText("Switch to English" if GLOBAL_LANG == "CN" else "切换为中文")
        self.update_list()

    def update_list(self):
        self.list_widget.clear()
        for idx, name in enumerate(self.stories.keys()):
            display_text = f"{idx + 1}. {name}"
            if name == self.recent_story_name:
                display_text += TR(" (最近打开)")
            self.list_widget.addItem(display_text)

    def get_selected_name(self):
        row = self.list_widget.currentRow()
        if row >= 0 and row < len(self.stories):
            return list(self.stories.keys())[row]
        return None

    def make_top_story(self, name, data):
        new_stories = {name: data}
        for k, v in self.stories.items():
            if k != name:
                new_stories[k] = v
        self.stories = new_stories
        self.recent_story_name = name
        self.update_list()

    def new_story(self):
        text, ok = QInputDialog.getText(self, TR('新建'), TR('输入故事线名称:'))
        if ok and text:
            if text in self.stories:
                QMessageBox.warning(self, TR("错误"), TR("名称已存在！"))
                return
            self.stories[text] = None
            self.update_list()
            
    def open_story_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, TR("打开故事线文件"), "", "JSON Files (*.json);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                name = os.path.basename(file_path)
                self.make_top_story(name, state)
            except Exception as e:
                QMessageBox.critical(self, TR("错误"), TR("打开文件失败:") + f" {e}")
                
    def rename_story(self):
        name = self.get_selected_name()
        if not name: return
        new_name, ok = QInputDialog.getText(self, TR('重命名'), TR('输入新的故事线名称:'), text=name)
        if ok and new_name and new_name != name:
            if new_name in self.stories:
                QMessageBox.warning(self, TR("错误"), TR("名称已存在！"))
                return
            
            new_stories = {}
            for k, v in self.stories.items():
                if k == name:
                    new_stories[new_name] = v
                else:
                    new_stories[k] = v
            self.stories = new_stories
            if self.recent_story_name == name:
                self.recent_story_name = new_name
            self.update_list()

    def edit_story(self):
        name = self.get_selected_name()
        if not name: return
        self.main_window.current_story_name = name
        scene = self.main_window.outline_widget.scene
        
        scene.clear_scene_completely()
        scene.history.clear()
        
        state = self.stories.get(name)
        if state:
            scene.deserialize_scene(state)
            scene.save_history() 
        else:
            scene.add_node("Start", QPointF(0,0))
            scene.save_history() 
            
        scene.set_dirty(False)
        self.main_window.outline_widget.update_title()
        self.main_window.stacked.setCurrentIndex(1)

    def export_story_list(self):
        name = self.get_selected_name()
        if not name: return
        file_path, _ = QFileDialog.getSaveFileName(self, TR("另存为故事线"), name, "JSON Files (*.json);;All Files (*)")
        if file_path:
            try:
                state = self.stories.get(name)
                if not state:
                    state = {"nodes": [], "edges": []}
                else:
                    state = filter_export_state(state)
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(state, f, ensure_ascii=False, indent=4)
                QMessageBox.information(self, TR("成功"), TR("故事线已导出到:\n") + file_path)
            except Exception as e:
                QMessageBox.critical(self, TR("错误"), TR("导出失败: ") + str(e))
                
    def export_table_list_action(self):
        name = self.get_selected_name()
        if not name: return
        state = self.stories.get(name)
        if not state:
            QMessageBox.warning(self, TR("错误"), TR("当前故事线为空或无节点数据！"))
            return
        export_to_table(self, state, name)

    def delete_story(self):
        name = self.get_selected_name()
        if name and name in self.stories:
            text = TR("确定要删除故事线") + f" '{name}' " + TR("吗？\n此操作不可恢复！")
            reply = QMessageBox.question(self, TR('确认删除'), text,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                del self.stories[name]
                if self.recent_story_name == name:
                    self.recent_story_name = None
                self.update_list()

# ==========================================
# 5. 主窗口
# ==========================================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("故事线蓝图编辑器")
        self.resize(1280, 850)
        self.setMinimumSize(1024, 768)
        
        # 二次确保主窗口强制识别 ICO 任务栏/窗口图标
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "Resources", "Icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            
        self.current_story_name = None
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        
        self.list_widget = StoryListWidget(self)
        self.outline_widget = StoryOutlineWidget(self)
        
        self.stacked.addWidget(self.list_widget)
        self.stacked.addWidget(self.outline_widget)
        
        self.update_language()

    def update_language(self):
        if self.current_story_name:
            self.setWindowTitle(TR("编辑中 - ") + self.current_story_name)
        else:
            self.setWindowTitle(TR("故事线蓝图编辑器"))
        self.list_widget.update_ui_text()
        self.outline_widget.update_ui_text()

    def closeEvent(self, event):
        if self.stacked.currentIndex() == 1 and self.outline_widget.scene._is_dirty:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle(TR("未保存提示"))
            msg_box.setText(TR("故事线尚未保存，是否保存后退出？"))
            btn_save = msg_box.addButton(TR("保存并退出"), QMessageBox.AcceptRole)
            btn_discard = msg_box.addButton(TR("不保存退出"), QMessageBox.DestructiveRole)
            btn_cancel = msg_box.addButton(TR("取消退出"), QMessageBox.RejectRole)
            msg_box.exec_()
            
            if msg_box.clickedButton() == btn_save:
                self.outline_widget.save_story()
                event.accept()
            elif msg_box.clickedButton() == btn_discard:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


# ==========================================
# 全局精美现代暗黑风格样式表
# ==========================================
GLOBAL_QSS = """
QWidget {
    font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
    color: #e0e0e0;
}
QMainWindow, QDialog {
    background-color: #1e1e1e;
}
#StoryListWidget, #StoryOutlineWidget {
    background-color: #1e1e1e;
}
#PropertyPanel {
    background-color: #252526;
    border: 1px solid #3e3e42;
    border-radius: 6px;
}
#PropertyContentWidget, #PropertyBranchContainer, #BranchWidget {
    background-color: transparent;
}
QScrollArea {
    background-color: transparent;
    border: none;
}
QScrollArea > QWidget > QWidget {
    background-color: transparent;
}
QGraphicsView {
    background-color: #121212;
}
QPushButton {
    background-color: #2d2d30;
    border: 1px solid #3e3e42;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: bold;
    color: #d4d4d4;
}
QPushButton:hover {
    background-color: #3e3e42;
    border-color: #4fc3f7;
    color: #ffffff;
}
QPushButton:pressed {
    background-color: #0277bd;
    border-color: #0277bd;
}
QListWidget {
    background-color: #252526;
    border: 1px solid #3e3e42;
    border-radius: 6px;
    padding: 8px;
    font-size: 15px;
    outline: none;
}
QListWidget::item {
    padding: 12px;
    border-radius: 4px;
    margin-bottom: 4px;
}
QListWidget::item:hover {
    background-color: #2a2d2e;
}
QListWidget::item:selected {
    background-color: #0277bd;
    color: white;
}
QLineEdit, QTextEdit, QComboBox {
    background-color: #333333;
    border: 1px solid #3e3e42;
    border-radius: 4px;
    padding: 6px;
    selection-background-color: #4fc3f7;
    color: #ffffff;
}
QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border: 1px solid #4fc3f7;
}
QComboBox::drop-down {
    border: none;
}
QComboBox QAbstractItemView {
    background-color: #333333;
    border: 1px solid #3e3e42;
    selection-background-color: #0277bd;
}
QSlider::groove:horizontal {
    border: 1px solid #3e3e42;
    height: 6px;
    background: #424242;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #4fc3f7;
    border: none;
    width: 14px;
    margin: -4px 0;
    border-radius: 7px;
}
QScrollBar:vertical {
    border: none;
    background-color: #2d2d30;
    width: 12px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background-color: #555555;
    border-radius: 6px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background-color: #777777;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    border: none;
    background: none;
}
QScrollBar:horizontal {
    border: none;
    background-color: #2d2d30;
    height: 12px;
    margin: 0px;
}
QScrollBar::handle:horizontal {
    background-color: #555555;
    border-radius: 6px;
    min-width: 20px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #777777;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    border: none;
    background: none;
}
"""

if __name__ == "__main__":
    # 强制在Windows系统中声明独立的应用程序ID，以确保任务栏能正确加载和显示自定义的窗口图标
    try:
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("wuguanyu.storyeditor.1.0")
    except Exception:
        pass

    app = QApplication(sys.argv)
    
    # 获取运行目录逻辑，兼容打包环境
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    icon_path = os.path.join(base_dir, "Resources", "Icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    app.setStyle("Fusion")
    app.setStyleSheet(GLOBAL_QSS)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

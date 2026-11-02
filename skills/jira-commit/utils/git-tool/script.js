// Git工具的JavaScript逻辑

// 返回主页面
function goBack() {
    if (window.parent && window.parent.toolManager) {
        window.parent.toolManager.showMain();
    } else if (window.parent && window.parent.showMain) {
        window.parent.showMain();
    } else {
        alert('当前为独立模式，无法返回主页面');
    }
}

// 表单操作相关
const form = document.getElementById('commit-form');
const formElements = form ? form.elements : [];

function saveForm() {
    const data = {};
    for (const element of formElements) {
        if (element.id) {
            if (element.type === 'checkbox') {
                data[element.id] = element.checked;
            } else {
                data[element.id] = element.value;
            }
        }
    }
    localStorage.setItem('commitFormData', JSON.stringify(data));
    localStorage.removeItem('commitFormData_before_reset');
}

function populateForm(data) {
    for (const id in data) {
        const element = document.getElementById(id);
        if (element) {
            if (element.type === 'checkbox') {
                element.checked = data[id];
            } else {
                element.value = data[id];
            }
        }
    }
    toggleInput('module', document.getElementById('enable_module').checked);
    toggleInput('customer_name', document.getElementById('enable_customer').checked);
    toggleInput('part_info', document.getElementById('enable_part').checked);
}

function loadForm() {
    const data = JSON.parse(localStorage.getItem('commitFormData'));
    if (data) {
        populateForm(data);
    }
}

function toggleInput(inputId, isEnabled) {
    const inputElement = document.getElementById(inputId);
    if (inputElement) {
        inputElement.disabled = !isEnabled;
        if (!isEnabled) {
            inputElement.value = '';
        }
    }
}

function undoForm() {
    const undoData = localStorage.getItem('commitFormData_before_reset');
    if (undoData && undoData !== 'null') { 
        const data = JSON.parse(undoData);
        populateForm(data);
        saveForm(); 
        alert('已成功撤回至清空前的内容！');
    } else {
        alert('没有可撤回的操作。请先清空表单。');
    }
}

function resetForm() {
    if (confirm('确定要清空表单内容吗？')) {
        const currentData = localStorage.getItem('commitFormData');
        if (currentData && currentData !== '{}') {
            localStorage.setItem('commitFormData_before_reset', currentData);
        } else {
            localStorage.removeItem('commitFormData_before_reset');
        }

        form.reset();
        localStorage.removeItem('commitFormData');
        toggleInput('module', false);
        toggleInput('customer_name', false);
        toggleInput('part_info', false);
    }
}

function clearLog() {
    const output = document.getElementById('output');
    if (output) {
        output.value = '';
    }
}

async function copyToClipboard() {
    const output = document.getElementById('output');
    if (!output || !output.value) {
        alert('没有可复制的内容。');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(output.value);
        alert('已复制到剪贴板！');
    } catch (err) {
        // 降级方案
        output.select();
        document.execCommand('copy');
        alert('已复制到剪贴板！');
    }
}

function generate() {
    const commitMode = document.getElementById('commit_mode').value;
    
    if (commitMode === 'single') {
        generateSingleCommit();
    } else {
        generateMultipleCommits();
    }
}

function generateSingleCommit() {
    const summaryEnElement = document.getElementById('summary_en');

    const commit_type = document.getElementById('commit_type').value;
    const module = document.getElementById('enable_module').checked ? document.getElementById('module').value : '';
    const jira_id = document.getElementById('jira_id').value.trim();
    const customer_name = document.getElementById('customer_name').value;
    const part_info = document.getElementById('part_info').value;
    const summary_en = summaryEnElement.value;
    const what_cn = document.getElementById('what_cn').value;
    const why_cn = document.getElementById('why_cn').value;
    const how_cn = document.getElementById('how_cn').value;
    const impact_level = document.getElementById('impact_level').value;
    const test_scope = document.getElementById('test_scope').value;

    if (!summary_en.trim()) {
        alert('请填写摘要。');
        summaryEnElement.focus();
        return;
    }

    let header = `[${commit_type}]`;
    if (module) {
        header += `[${module}]`;
    }
    if (jira_id) {
        header += `[${jira_id}]`;
    }
    if (customer_name) {
        header += `[${customer_name}]`;
    }
    if (part_info) {
        header += `[Part ${part_info}]`;
    }
    header += summary_en;
    
    const body = `\n[what]${what_cn}\n` +
                 `[why]\n${why_cn}\n` +
                 `[how]\n${how_cn}\n` +
                 `[影响等级]${impact_level}\n` +
                 `[建议测试范围]${test_scope}`;

    const commitMessage = header + "\n" + body;

    document.getElementById('output').value = commitMessage;
}

function generateMultipleCommits() {
    const commit_type = document.getElementById('commit_type').value;
    const module = document.getElementById('enable_module').checked ? document.getElementById('module').value : '';
    const jira_ids = document.getElementById('jira_ids').value.trim();
    const commit_count = parseInt(document.getElementById('commit_count').value);
    
    if (!jira_ids) {
        alert('请填写JIRA ID列表。');
        return;
    }
    
    const jiraIdArray = jira_ids.split(',').map(id => id.trim()).filter(id => id);
    
    if (jiraIdArray.length === 0) {
        alert('请填写有效的JIRA ID列表。');
        return;
    }
    
    // 生成总标题
    let header = `[${commit_type}]`;
    if (module) {
        header += `[${module}]`;
    }
    jiraIdArray.forEach(jiraId => {
        header += `[${jiraId}]`;
    });
    header += ` ${commit_count} commits`;
    
    let result = header + '\n\n';
    
    // 生成每个commit的详细信息
    for (let i = 0; i < commit_count; i++) {
        const jiraId = jiraIdArray[i] || jiraIdArray[0]; // 如果JIRA ID不够用，重复使用第一个
        
        // 获取对应commit的表单数据
        const summaryEn = document.getElementById(`commit_${i}_summary_en`)?.value || '';
        const whatCn = document.getElementById(`commit_${i}_what_cn`)?.value || '';
        const whyCn = document.getElementById(`commit_${i}_why_cn`)?.value || '';
        const howCn = document.getElementById(`commit_${i}_how_cn`)?.value || '';
        const impactLevel = document.getElementById(`commit_${i}_impact_level`)?.value || 'B';
        const testScope = document.getElementById(`commit_${i}_test_scope`)?.value || '';
        
        let commitHeader = `[${commit_type}]`;
        if (module) {
            commitHeader += `[${module}]`;
        }
        commitHeader += `[${jiraId}]${summaryEn}`;
        
        const commitBody = `\n[what]${whatCn}\n` +
                          `[why]\n${whyCn}\n` +
                          `[how]\n${howCn}\n` +
                          `[影响等级]${impactLevel}\n` +
                          `[建议测试范围]${testScope}`;
        
        result += commitHeader + '\n' + commitBody + '\n\n';
    }
    
    document.getElementById('output').value = result.trim();
}

function toggleCommitMode() {
    const commitMode = document.getElementById('commit_mode').value;
    const singleSection = document.getElementById('single-commit-section');
    const multipleSection = document.getElementById('multiple-commits-section');
    const singleJiraSection = document.getElementById('single-jira-section');
    
    if (commitMode === 'single') {
        singleSection.style.display = 'block';
        multipleSection.style.display = 'none';
        singleJiraSection.style.display = 'block';
    } else {
        singleSection.style.display = 'none';
        multipleSection.style.display = 'block';
        singleJiraSection.style.display = 'none';
        generateCommitForms();
    }
}

function generateCommitForms() {
    const commitCount = parseInt(document.getElementById('commit_count').value);
    const container = document.getElementById('commits-container');
    const commitControls = document.getElementById('commit-controls');
    
    container.innerHTML = '';
    
    // 显示控制按钮（当有多个commit时）
    if (commitCount > 1) {
        commitControls.style.display = 'block';
    } else {
        commitControls.style.display = 'none';
    }
    
    for (let i = 0; i < commitCount; i++) {
        const commitDiv = document.createElement('div');
        commitDiv.className = 'commit-form';
        commitDiv.style.border = '1px solid #ddd';
        commitDiv.style.padding = '15px';
        commitDiv.style.margin = '10px 0';
        commitDiv.style.borderRadius = '6px';
        commitDiv.style.backgroundColor = '#f8f9fa';
        
        commitDiv.innerHTML = `
            <div class="commit-header" onclick="toggleCommitForm(${i})" style="cursor: pointer; display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #ddd; margin-bottom: 10px;">
                <h4 style="margin: 0;">Commit ${i + 1}</h4>
                <span id="commit_${i}_toggle" class="toggle-icon" style="font-size: 18px; font-weight: bold;">▼</span>
            </div>
            <div id="commit_${i}_content" class="commit-content">
                <div class="form-group">
                    <label for="commit_${i}_summary_en">摘要</label>
                    <input type="text" id="commit_${i}_summary_en" placeholder="languageSetting">
                </div>
                <div class="form-group">
                    <label for="commit_${i}_what_cn"><strong>[what]</strong> 中文描述 (问题现象)</label>
                    <textarea id="commit_${i}_what_cn" rows="3" placeholder="0x534 languageSetting1外发报文添加记忆功能"></textarea>
                </div>
                <div class="form-group">
                    <label for="commit_${i}_why_cn"><strong>[why]</strong> 中文描述 (问题原因)</label>
                    <textarea id="commit_${i}_why_cn" rows="3" placeholder="0x534 languageSetting1外发报文添加记忆功能"></textarea>
                </div>
                <div class="form-group">
                    <label for="commit_${i}_how_cn"><strong>[how]</strong> 中文描述 (解决方法)</label>
                    <textarea id="commit_${i}_how_cn" rows="3" placeholder="0x534 languageSetting1外发报文添加记忆功能"></textarea>
                </div>
                <div class="form-group">
                    <label for="commit_${i}_impact_level"><strong>[影响等级]</strong></label>
                    <select id="commit_${i}_impact_level">
                        <option value="S">S (系统级)</option>
                        <option value="A" selected>A (应用级)</option>
                        <option value="B">B (模块级)</option>
                        <option value="C">C (组件级)</option>
                        <option value="D">D (细节级)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="commit_${i}_test_scope"><strong>[测试范围]</strong></label>
                    <textarea id="commit_${i}_test_scope" rows="2" placeholder=""></textarea>
                </div>
            </div>
        `;
        
        container.appendChild(commitDiv);
    }
}

function toggleCommitForm(index) {
    const content = document.getElementById(`commit_${index}_content`);
    const toggle = document.getElementById(`commit_${index}_toggle`);
    
    if (content.style.display === 'none') {
        content.style.display = 'block';
        toggle.textContent = '▼';
    } else {
        content.style.display = 'none';
        toggle.textContent = '▶';
    }
}

function toggleAllCommits() {
    const commitCount = parseInt(document.getElementById('commit_count').value);
    const toggleAllBtn = document.getElementById('toggle-all-btn');
    const isCurrentlyExpanded = toggleAllBtn.textContent === '折叠所有表单';
    
    for (let i = 0; i < commitCount; i++) {
        const content = document.getElementById(`commit_${i}_content`);
        const toggle = document.getElementById(`commit_${i}_toggle`);
        
        if (isCurrentlyExpanded) {
            // 折叠所有
            content.style.display = 'none';
            toggle.textContent = '▶';
        } else {
            // 展开所有
            content.style.display = 'block';
            toggle.textContent = '▼';
        }
    }
    
    // 更新按钮文本
    toggleAllBtn.textContent = isCurrentlyExpanded ? '展开所有表单' : '折叠所有表单';
}

// 初始化工具
function initTool() {
    console.log('Git工具已初始化');
    
    // 检查运行环境
    const isElectron = typeof window.electronAPI !== 'undefined';
    const isIntegrated = window.parent !== window;
    
    console.log('Git工具运行环境:', {
        isElectron: isElectron,
        isIntegrated: isIntegrated
    });
    
    // 如果是集成模式，显示返回按钮
    if (isIntegrated) {
        const backButton = document.querySelector('.back-button');
        if (backButton) {
            backButton.style.display = 'inline-block';
        }
    }
    
    // 加载保存的表单数据
    loadForm();
    
    // 设置事件监听
    if (formElements.length > 0) {
        for (const element of formElements) {
            element.addEventListener('input', saveForm);
        }
    }
    
    // 初始化输入框状态
    toggleInput('module', document.getElementById('enable_module')?.checked || false);
    toggleInput('customer_name', document.getElementById('enable_customer')?.checked || false);
    toggleInput('part_info', document.getElementById('enable_part')?.checked || false);
    
    // 初始化提交模式
    toggleCommitMode();
}

// 页面加载完成后初始化
window.addEventListener('load', initTool);
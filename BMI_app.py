import streamlit as st

# 页面标题
st.set_page_config(page_title="BMI 计算器", page_icon="💪", layout="centered")

st.title("💪 BMI 计算器")

st.markdown("输入你的体重和身高，看看你目前的身体状况吧！")

# 输入栏
weight = st.number_input("请输入体重 (kg)：", min_value=0.0, step=0.1)
height = st.number_input("请输入身高 (m)：", min_value=0.0, step=0.01)

# 计算按钮
if st.button("计算 BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.write(f"### 你的 BMI 是：**{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("还没死吗hmm..")
        elif bmi <= 24.9:
            st.success("是个人物居然可以那么正常")
        elif bmi <= 29.9:
            st.info("md,死肥仔,gnn")
        else:
            st.error("ejz Pro Max 版")
    else:
        st.error("请输入有效的身高和体重！")

# 页脚
st.markdown("---")
st.caption("由 Streamlit 构建 | 作者：LKM 😄")

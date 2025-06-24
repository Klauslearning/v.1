
import streamlit as st
import pandas as pd
from utils import get_commodity_code, estimate_weight

st.title("📦 DHL CSV 自动生成工具（带前端编辑功能）")

uploaded_file = st.file_uploader("上传包含商品描述的 Excel 文件", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=0)
    st.write("数据预览：", df.head())

    # 提取并构建输出结构
    output_rows = []
    for idx, row in df.iterrows():
        desc = str(row.get("Item Description", "")).strip()
        qty = int(row.get("Quantity", 1))
        val = float(row.get("Value", 1))
        currency = row.get("Currency", "GBP")

        code = get_commodity_code(desc)
        weight = estimate_weight(desc)

        output_rows.append({
            "Item Description": desc,
            "Commodity Code": code,
            "Quantity": qty,
            "Units": "PCS",
            "Value": val,
            "Currency": currency,
            "Weight": weight,
            "Country of Origin": "CN"
        })

    editable_df = pd.DataFrame(output_rows)

    st.subheader("✏️ 审核并修改以下字段：")
    edited_df = st.data_editor(
        editable_df,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Weight": st.column_config.NumberColumn(format="%.2f"),
            "Commodity Code": st.column_config.TextColumn(),
            "Country of Origin": st.column_config.TextColumn()
        }
    )

    if st.button("✅ 生成最终 DHL CSV"):
        final_df = edited_df.copy()
        final_df.insert(0, "Unique Item Number", range(1, len(final_df) + 1))
        final_df.insert(1, "Item", "INV_ITEM")
        final_df["Weight 2"] = ""
        final_df["Reference Type"] = ""
        final_df["Reference Details"] = ""
        final_df["Tax Paid"] = "N"

        column_order = ["Unique Item Number", "Item", "Item Description", "Commodity Code",
                        "Quantity", "Units", "Value", "Currency", "Weight", "Weight 2",
                        "Country of Origin", "Reference Type", "Reference Details", "Tax Paid"]

        final_df = final_df[column_order]

        st.download_button(
            label="📥 下载 DHL 上传格式 CSV（无表头）",
            data=final_df.to_csv(index=False, header=False).encode("utf-8-sig"),
            file_name="dhl_final.csv",
            mime="text/csv"
        )

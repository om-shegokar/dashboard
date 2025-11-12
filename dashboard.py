import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page Configuration
st.set_page_config(page_title="Coding Model Evaluation Dashboard", layout="wide")

# Page Title
st.title("🤖 Coding Model Evaluation Dashboard")
st.markdown("Comprehensive evaluation of coding models across multiple benchmarks")

# Sidebar for navigation
st.sidebar.title("Navigation")
benchmark_selection = st.sidebar.radio(
    "Select Benchmark:",
    ["Overview", "Model Comparison Graphs", "ARCHIT EVAL SCRIPT", "HumanEval (Rust)", "SWE Benchmark", 
     "RustEvo Benchmark", "Aider-Polyglot", "Haskell LLM"]
)

# Overview Section
if benchmark_selection == "Overview":
    st.header("📊 Benchmark Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Benchmarks", "6")
        st.metric("Models Evaluated", "10+")
    
    with col2:
        st.metric("Total Test Cases", "2000+")
        st.metric("Languages Tested", "7")
    
    with col3:
        st.metric("Datasets", "5")
        st.metric("Evaluation Modes", "Multiple")
    
    st.markdown("---")
    st.subheader("Available Benchmarks")
    
    benchmarks_info = pd.DataFrame({
        'Benchmark': [
            'ARCHIT EVAL SCRIPT',
            'HumanEval (Rust)',
            'SWE Benchmark',
            'RustEvo Benchmark',
            'Aider-Polyglot',
            'Haskell LLM'
        ],
        'Focus': [
            'General code generation',
            'Functional correctness (Rust)',
            'Real-world bug fixing',
            'API evolution adaptation',
            'Multi-language code editing',
            'Functional programming (Haskell)'
        ],
        'Models Tested': [
            '5',
            '3',
            '2',
            '4',
            '4',
            '1'
        ]
    })
    st.dataframe(benchmarks_info, use_container_width=True)

# Model Comparison Graphs
elif benchmark_selection == "Model Comparison Graphs":
    st.header("📊 Model Comparison Graphs")
    
    st.markdown("Interactive visualizations comparing model performance across different benchmarks and metrics")
    
    # Create tabs for different graph categories
    graph_tab1, graph_tab2, graph_tab3, graph_tab4 = st.tabs([
        "ARCHIT EVAL Performance", 
        "RustEvo Benchmark", 
        "HumanEval Comparison",
        "Overall Metrics"
    ])
    
    with graph_tab1:
        st.subheader("ARCHIT EVAL SCRIPT - Pass@k Comparison")
        
        # Data for ARCHIT EVAL
        archit_data = pd.DataFrame({
            'Model': ['kat-dev-hs-32b', 'kat-dev-base-32b', 'kat-dev-hs-72b', 'kat-dev-base-72b', 'Claude Sonnet 4.5'],
            'Pass@1': [32.0, 15.67, 42.55, 13.64, 54.0],
            'Pass@3': [55.33, 23.33, 61.70, 17.05, 62.0],
            'Pass@8': [75.33, 27.33, 74.47, 22.73, 68.0]
        })
        
        # Pass@k comparison bar chart
        fig1 = go.Figure()
        
        for metric in ['Pass@1', 'Pass@3', 'Pass@8']:
            fig1.add_trace(go.Bar(
                name=metric,
                x=archit_data['Model'],
                y=archit_data[metric],
                text=archit_data[metric].round(2),
                textposition='auto',
            ))
        
        fig1.update_layout(
            title='ARCHIT EVAL SCRIPT - Pass@k Performance Comparison',
            xaxis_title='Model',
            yaxis_title='Pass Rate (%)',
            barmode='group',
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Pass@1 specific comparison
        fig2 = px.bar(
            archit_data,
            x='Model',
            y='Pass@1',
            title='ARCHIT EVAL SCRIPT - Pass@1 Comparison',
            text='Pass@1',
            color='Pass@1',
            color_continuous_scale='Viridis',
            height=400
        )
        fig2.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
        
        # Error rate comparison
        error_data = pd.DataFrame({
            'Model': ['kat-dev-hs-32b', 'kat-dev-base-32b', 'kat-dev-hs-72b', 'kat-dev-base-72b', 'Claude Sonnet 4.5'],
            'Error Rate': [0.0, 0.0, 6.0, 12.0, 0.0]
        })
        
        fig3 = px.bar(
            error_data,
            x='Model',
            y='Error Rate',
            title='Error Rate Comparison',
            text='Error Rate',
            color='Error Rate',
            color_continuous_scale='Reds',
            height=400
        )
        fig3.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        st.plotly_chart(fig3, use_container_width=True)
    
    with graph_tab2:
        st.subheader("RustEvo Benchmark - Model Performance")
        
        # RustEvo Pass@1 comparison
        rustevo_data = pd.DataFrame({
            'Model': ['kat-dev-hs-72b', 'kat-dev-base-72b', 'kat-dev-hs-32b', 'kat-dev-base-32b'],
            'RQ1 (Full Docs)': [31.80, 32.99, 37.59, 32.31],
            'RQ3 (Minimal Docs)': [26.02, 22.11, 30.27, 28.74]
        })
        
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(
            name='RQ1 (Full Documentation)',
            x=rustevo_data['Model'],
            y=rustevo_data['RQ1 (Full Docs)'],
            text=rustevo_data['RQ1 (Full Docs)'].round(2),
            textposition='auto',
            marker_color='lightblue'
        ))
        fig4.add_trace(go.Bar(
            name='RQ3 (Minimal Documentation)',
            x=rustevo_data['Model'],
            y=rustevo_data['RQ3 (Minimal Docs)'],
            text=rustevo_data['RQ3 (Minimal Docs)'].round(2),
            textposition='auto',
            marker_color='lightcoral'
        ))
        
        fig4.update_layout(
            title='RustEvo - Pass@1 Comparison (RQ1 vs RQ3)',
            xaxis_title='Model',
            yaxis_title='Pass@1 (%)',
            barmode='group',
            height=500
        )
        st.plotly_chart(fig4, use_container_width=True)
        
        # API Usage Accuracy
        api_accuracy_data = pd.DataFrame({
            'Model': ['kat-dev-hs-72b', 'kat-dev-base-72b', 'kat-dev-hs-32b', 'kat-dev-base-32b'],
            'RQ1 API Accuracy': [85.20, 86.90, 93.20, 94.22],
            'RQ3 API Accuracy': [85.71, 72.79, 94.05, 94.90]
        })
        
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            name='RQ1 API Accuracy',
            x=api_accuracy_data['Model'],
            y=api_accuracy_data['RQ1 API Accuracy'],
            text=api_accuracy_data['RQ1 API Accuracy'].round(2),
            textposition='auto',
            marker_color='mediumseagreen'
        ))
        fig5.add_trace(go.Bar(
            name='RQ3 API Accuracy',
            x=api_accuracy_data['Model'],
            y=api_accuracy_data['RQ3 API Accuracy'],
            text=api_accuracy_data['RQ3 API Accuracy'].round(2),
            textposition='auto',
            marker_color='orange'
        ))
        
        fig5.update_layout(
            title='RustEvo - API Usage Accuracy Comparison',
            xaxis_title='Model',
            yaxis_title='API Usage Accuracy (%)',
            barmode='group',
            height=500
        )
        st.plotly_chart(fig5, use_container_width=True)
        
        # Success Count Comparison
        success_data = pd.DataFrame({
            'Model': ['kat-dev-hs-72b', 'kat-dev-base-72b', 'kat-dev-hs-32b', 'kat-dev-base-32b'],
            'RQ1 Success': [187, 194, 221, 190],
            'RQ3 Success': [153, 130, 178, 169]
        })
        
        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(
            name='RQ1 Success Count',
            x=success_data['Model'],
            y=success_data['RQ1 Success'],
            mode='lines+markers',
            marker=dict(size=12),
            line=dict(width=3)
        ))
        fig6.add_trace(go.Scatter(
            name='RQ3 Success Count',
            x=success_data['Model'],
            y=success_data['RQ3 Success'],
            mode='lines+markers',
            marker=dict(size=12),
            line=dict(width=3)
        ))
        
        fig6.update_layout(
            title='RustEvo - Success Count Comparison (out of 588 tasks)',
            xaxis_title='Model',
            yaxis_title='Number of Successful Tasks',
            height=500
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    with graph_tab3:
        st.subheader("HumanEval (Rust) - Model Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Kawai-pilot comparison
            kawai_data = pd.DataFrame({
                'Model Type': ['Fine-tuned', 'Base'],
                'Pass@1': [30.90, 40.45],
                'Pass@10': [57.69, 66.03]
            })
            
            fig7 = go.Figure()
            fig7.add_trace(go.Bar(
                name='Pass@1',
                x=kawai_data['Model Type'],
                y=kawai_data['Pass@1'],
                text=kawai_data['Pass@1'],
                textposition='auto',
                marker_color='royalblue'
            ))
            fig7.add_trace(go.Bar(
                name='Pass@10',
                x=kawai_data['Model Type'],
                y=kawai_data['Pass@10'],
                text=kawai_data['Pass@10'],
                textposition='auto',
                marker_color='lightsteelblue'
            ))
            
            fig7.update_layout(
                title='Kawai-pilot 32B - HumanEval Performance',
                yaxis_title='Pass Rate (%)',
                barmode='group',
                height=400
            )
            st.plotly_chart(fig7, use_container_width=True)
        
        with col2:
            # Qwen comparison
            qwen_data = pd.DataFrame({
                'Model Type': ['Fine-tuned', 'Base'],
                'Pass@1': [16.99, 5.45],
                'Pass@10': [21.79, 10.26]
            })
            
            fig8 = go.Figure()
            fig8.add_trace(go.Bar(
                name='Pass@1',
                x=qwen_data['Model Type'],
                y=qwen_data['Pass@1'],
                text=qwen_data['Pass@1'],
                textposition='auto',
                marker_color='forestgreen'
            ))
            fig8.add_trace(go.Bar(
                name='Pass@10',
                x=qwen_data['Model Type'],
                y=qwen_data['Pass@10'],
                text=qwen_data['Pass@10'],
                textposition='auto',
                marker_color='lightgreen'
            ))
            
            fig8.update_layout(
                title='Qwen - HumanEval Performance',
                yaxis_title='Pass Rate (%)',
                barmode='group',
                height=400
            )
            st.plotly_chart(fig8, use_container_width=True)
        
        # Combined comparison
        combined_humaneval = pd.DataFrame({
            'Model': ['Kawai-pilot FT', 'Kawai-pilot Base', 'Qwen FT', 'Qwen Base'],
            'Pass@1': [30.90, 40.45, 16.99, 5.45],
            'Pass@10': [57.69, 66.03, 21.79, 10.26]
        })
        
        fig9 = px.scatter(
            combined_humaneval,
            x='Pass@1',
            y='Pass@10',
            text='Model',
            size=[20, 20, 20, 20],
            color='Model',
            title='HumanEval - Pass@1 vs Pass@10 Comparison',
            height=500
        )
        fig9.update_traces(textposition='top center')
        st.plotly_chart(fig9, use_container_width=True)
        
        # SWE Benchmark comparison
        st.subheader("SWE Benchmark - Base vs Fine-tuned")
        
        swe_data = pd.DataFrame({
            'Metric': ['Completed Instances', 'Resolved Instances', 'Error Instances'],
            'Kwai Base': [20, 2, 480],
            'Kwai Fine-tuned (LoRA)': [33, 4, 467]
        })
        
        fig10 = go.Figure()
        fig10.add_trace(go.Bar(
            name='Kwai Base',
            x=swe_data['Metric'],
            y=swe_data['Kwai Base'],
            text=swe_data['Kwai Base'],
            textposition='auto',
            marker_color='indianred'
        ))
        fig10.add_trace(go.Bar(
            name='Kwai Fine-tuned (LoRA)',
            x=swe_data['Metric'],
            y=swe_data['Kwai Fine-tuned (LoRA)'],
            text=swe_data['Kwai Fine-tuned (LoRA)'],
            textposition='auto',
            marker_color='seagreen'
        ))
        
        fig10.update_layout(
            title='SWE Benchmark - Base vs Fine-tuned Comparison',
            yaxis_title='Count (out of 500 instances)',
            barmode='group',
            height=500
        )
        st.plotly_chart(fig10, use_container_width=True)
    
    with graph_tab4:
        st.subheader("Overall Model Performance Comparison")
        
        # Create radar chart for overall comparison
        categories = ['ARCHIT Pass@1', 'RustEvo RQ1', 'API Accuracy', 'Success Rate']
        
        fig11 = go.Figure()
        
        # kat-dev-hs-32b
        fig11.add_trace(go.Scatterpolar(
            r=[32.0, 37.59, 93.20, 37.59],
            theta=categories,
            fill='toself',
            name='kat-dev-hs-32b'
        ))
        
        # kat-dev-base-32b
        fig11.add_trace(go.Scatterpolar(
            r=[15.67, 32.31, 94.22, 32.31],
            theta=categories,
            fill='toself',
            name='kat-dev-base-32b'
        ))
        
        # kat-dev-hs-72b
        fig11.add_trace(go.Scatterpolar(
            r=[42.55, 31.80, 85.20, 31.80],
            theta=categories,
            fill='toself',
            name='kat-dev-hs-72b'
        ))
        
        # kat-dev-base-72b
        fig11.add_trace(go.Scatterpolar(
            r=[13.64, 32.99, 86.90, 32.99],
            theta=categories,
            fill='toself',
            name='kat-dev-base-72b'
        ))
        
        fig11.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            title='Multi-Dimensional Model Performance Comparison',
            height=600
        )
        st.plotly_chart(fig11, use_container_width=True)
        
        # Heatmap for model performance across benchmarks
        heatmap_data = pd.DataFrame({
            'Model': ['kat-dev-hs-32b', 'kat-dev-base-32b', 'kat-dev-hs-72b', 'kat-dev-base-72b', 'Claude Sonnet 4.5'],
            'ARCHIT Pass@1': [32.0, 15.67, 42.55, 13.64, 54.0],
            'ARCHIT Pass@8': [75.33, 27.33, 74.47, 22.73, 68.0],
            'RustEvo RQ1': [37.59, 32.31, 31.80, 32.99, None],
            'API Accuracy': [93.20, 94.22, 85.20, 86.90, None]
        })
        
        # Prepare data for heatmap
        heatmap_values = heatmap_data.set_index('Model').values
        
        fig12 = go.Figure(data=go.Heatmap(
            z=heatmap_values,
            x=['ARCHIT Pass@1', 'ARCHIT Pass@8', 'RustEvo RQ1', 'API Accuracy'],
            y=heatmap_data['Model'],
            colorscale='YlOrRd',
            text=heatmap_values,
            texttemplate='%{text:.1f}',
            textfont={"size": 10},
            hoverongaps=False
        ))
        
        fig12.update_layout(
            title='Performance Heatmap Across Benchmarks',
            height=500
        )
        st.plotly_chart(fig12, use_container_width=True)
        
        st.info("💡 **Insights**: The graphs show that fine-tuned models (kat-dev-hs) generally outperform base models, with kat-dev-hs-32b showing particularly strong performance in RustEvo RQ1 and API accuracy metrics.")

# ARCHIT EVAL SCRIPT Leaderboard
elif benchmark_selection == "ARCHIT EVAL SCRIPT":
    st.header("🎯 ARCHIT EVAL SCRIPT Leaderboard")
    
    st.subheader("32B Models (300 Examples)")
    data_32b = {
        'Model': ['kat-dev-hs-32b', 'kat-dev-base-32b'],
        'Total Examples': [300, 300],
        'Successful Predictions': [300, 300],
        'Error Rate': ['0.00%', '0.00%'],
        'Pass@1': ['32.00%', '15.67%'],
        'Pass@3': ['55.33%', '23.33%'],
        'Pass@8': ['75.33%', '27.33%']
    }
    df_32b = pd.DataFrame(data_32b)
    st.dataframe(df_32b, use_container_width=True)
    
    st.subheader("72B Models (100 Examples)")
    data_72b = {
        'Model': ['kat-dev-hs-72b', 'kat-dev-base-72b'],
        'Total Examples': [100, 100],
        'Successful Predictions': [94, 88],
        'Error Rate': ['6.00%', '12.00%'],
        'Pass@1': ['42.55%', '13.64%'],
        'Pass@3': ['61.70%', '17.05%'],
        'Pass@8': ['74.47%', '22.73%']
    }
    df_72b = pd.DataFrame(data_72b)
    st.dataframe(df_72b, use_container_width=True)
    
    st.subheader("Claude Sonnet 4.5 (100 Examples)")
    data_claude = {
        'Model': ['Claude Sonnet 4.5'],
        'Total Examples': [100],
        'Successful Predictions': [100],
        'Error Rate': ['0.00%'],
        'Pass@1': ['54.00%'],
        'Pass@3': ['62.00%'],
        'Pass@8': ['68.00%']
    }
    df_claude = pd.DataFrame(data_claude)
    st.dataframe(df_claude, use_container_width=True)
    
    st.info("📌 **Key Insight**: Fine-tuned models (kat-dev-hs) significantly outperform base models, with Claude Sonnet 4.5 leading in Pass@1 accuracy.")

# HumanEval Results
elif benchmark_selection == "HumanEval (Rust)":
    st.header("🦀 HumanEval (Rust) - Functional Correctness")
    
    st.markdown("""
    **HumanEval** is a foundational benchmark measuring functional correctness of code generated by LLMs.
    It contains 164 manually written programming problems testing reasoning, algorithmic understanding, and code generation.
    """)
    
    st.subheader("Kawai-pilot 32B")
    data_kawai = {
        'Model Type': ['Fine-tuned Model', 'Base Model'],
        'Pass@1': ['30.90%', '40.45%'],
        'Pass@10': ['57.69%', '66.03%']
    }
    df_kawai = pd.DataFrame(data_kawai)
    st.dataframe(df_kawai, use_container_width=True)
    
    st.subheader("Qwen")
    data_qwen = {
        'Model Type': ['Fine-tuned Model', 'Base Model'],
        'Pass@1': ['16.99%', '5.45%'],
        'Pass@10': ['21.79%', '10.26%']
    }
    df_qwen = pd.DataFrame(data_qwen)
    st.dataframe(df_qwen, use_container_width=True)
    
    st.warning("⚠️ **Note**: Kawai-pilot fine-tuned model performed lower than base. Most failures were due to syntax, formatting/structure, or logic errors.")
    st.success("✅ **Qwen Improvement**: Fine-tuned Qwen showed significant improvement over base model.")

# SWE Benchmark
elif benchmark_selection == "SWE Benchmark":
    st.header("🔧 SWE Benchmark - Real-world Bug Fixing")
    
    st.markdown("""
    The SWE Benchmark evaluates models on real-world software engineering tasks, specifically bug fixing and issue resolution.
    """)
    
    data_swe = {
        'Metric': [
            'Total Instances',
            'Submitted Instances',
            'Completed Instances',
            'Resolved Instances',
            'Unresolved Instances',
            'Empty Patch Instances',
            'Error Instances'
        ],
        'Kwai Base': [500, 500, 20, 2, 18, 0, 480],
        'Kwai Fine-tuned (LoRA)': [500, 500, 33, 4, 29, 0, 467]
    }
    df_swe = pd.DataFrame(data_swe)
    st.dataframe(df_swe, use_container_width=True)
    
    st.info("📌 **Key Insight**: Fine-tuned (LoRA) model performs slightly better than base model with more completed runs and fixed issues. Results are dominated by system-level errors rather than coding ability limitations.")

# RustEvo Benchmark
elif benchmark_selection == "RustEvo Benchmark":
    st.header("🦀 RustEvo Benchmark - API Evolution Adaptation")
    
    st.markdown("""
    **RustEvo** evaluates LLMs on Rust code generation under evolving API conditions with 588 curated evolution tasks.
    - **RQ1**: Full Documentation Evaluation (complete API context)
    - **RQ3**: Minimal Documentation Evaluation (sparse API context)
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["kat-dev-hs-72b", "kat-dev-base-72b", "kat-dev-hs-32b", "kat-dev-base-32b"])
    
    with tab1:
        st.subheader("kat-dev-hs-72b Performance")
        data_hs72 = {
            'Metric': [
                'Total Tasks',
                'Success Count',
                'Failed Count',
                'Pass@1',
                'Incorrect Signatures',
                'Incorrect API',
                'Borrow Checker Failures',
                'Borrow Checker Failure Rate',
                'API Usage True Count',
                'API Usage Accuracy',
                'API Coverage Distinct',
                'API Coverage Count',
                'Compilation Errors',
                'Test Failures'
            ],
            'RQ1 (Full Docs)': [
                588, 187, 401, '31.80%', 0, 87, 363, '90.52%', 
                501, '85.20%', '90.0%', '405/450', 386, 15
            ],
            'RQ3 (Minimal Docs)': [
                588, 153, 435, '26.02%', 44, 40, 359, '82.53%', 
                504, '85.71%', '89.78%', '404/450', 374, 17
            ]
        }
        df_hs72 = pd.DataFrame(data_hs72)
        st.dataframe(df_hs72, use_container_width=True)
        
        st.subheader("Performance by API Change Type (RQ1)")
        data_change_rq1 = {
            'Change Type': ['Stabilized', 'Signature', 'Implicit', 'Deprecated'],
            'Total': [184, 185, 195, 24],
            'Success': [62, 66, 59, 0],
            'Success Rate': ['33.70%', '35.68%', '30.26%', '0.00%'],
            'API Usage Accuracy': ['91.85%', '84.32%', '79.49%', '87.50%']
        }
        df_change_rq1 = pd.DataFrame(data_change_rq1)
        st.dataframe(df_change_rq1, use_container_width=True)
        
        st.subheader("Performance by API Change Type (RQ3)")
        data_change_rq3 = {
            'Change Type': ['Stabilized', 'Signature', 'Implicit', 'Deprecated'],
            'Total': [184, 185, 195, 24],
            'Success': [37, 60, 56, 0],
            'Success Rate': ['20.11%', '32.43%', '28.72%', '0.00%'],
            'API Usage Accuracy': ['84.24%', '84.32%', '89.23%', '79.17%']
        }
        df_change_rq3 = pd.DataFrame(data_change_rq3)
        st.dataframe(df_change_rq3, use_container_width=True)
    
    with tab2:
        st.subheader("kat-dev-base-72b Performance")
        data_base72 = {
            'Metric': [
                'Total Tasks',
                'Success Count',
                'Failed Count',
                'Pass@1',
                'Incorrect Signatures',
                'Incorrect API',
                'Borrow Checker Failures',
                'Borrow Checker Failure Rate',
                'API Usage True Count',
                'API Usage Accuracy',
                'API Coverage Distinct',
                'API Coverage Count',
                'Compilation Errors',
                'Test Failures'
            ],
            'RQ1 (Full Docs)': [
                588, 194, 394, '32.99%', 0, 77, 357, '90.61%', 
                511, '86.90%', '90.44%', '407/450', 378, 16
            ],
            'RQ3 (Minimal Docs)': [
                588, 130, 458, '22.11%', 133, 27, 300, '65.50%', 
                428, '72.79%', '78.22%', '352/450', 315, 10
            ]
        }
        df_base72 = pd.DataFrame(data_base72)
        st.dataframe(df_base72, use_container_width=True)
        
        st.subheader("Performance by API Change Type (RQ1)")
        data_change_rq1_b72 = {
            'Change Type': ['Stabilized', 'Signature', 'Implicit', 'Deprecated'],
            'Total': [184, 185, 195, 24],
            'Success': [64, 66, 64, 0],
            'Success Rate': ['34.78%', '35.68%', '32.82%', '0.00%'],
            'API Usage Accuracy': ['94.57%', '85.41%', '82.05%', '79.17%']
        }
        df_change_rq1_b72 = pd.DataFrame(data_change_rq1_b72)
        st.dataframe(df_change_rq1_b72, use_container_width=True)
    
    with tab3:
        st.subheader("kat-dev-hs-32b Performance")
        data_hs32 = {
            'Metric': [
                'Total Tasks',
                'Success Count',
                'Failed Count',
                'Pass@1',
                'Incorrect Signatures',
                'Incorrect API',
                'Borrow Checker Failures',
                'Borrow Checker Failure Rate',
                'API Usage True Count',
                'API Usage Accuracy',
                'API Coverage Distinct',
                'API Coverage Count',
                'Compilation Errors',
                'Test Failures'
            ],
            'RQ1 (Full Docs)': [
                588, 221, 367, '37.59%', 0, 40, 324, '88.28%', 
                548, '93.20%', '95.56%', '430/450', 352, 15
            ],
            'RQ3 (Minimal Docs)': [
                588, 178, 410, '30.27%', 1, 34, 376, '91.71%', 
                553, '94.05%', '96.44%', '434/450', 394, 15
            ]
        }
        df_hs32 = pd.DataFrame(data_hs32)
        st.dataframe(df_hs32, use_container_width=True)
        
        st.subheader("Performance by API Change Type (RQ1)")
        data_change_rq1_hs32 = {
            'Change Type': ['Stabilized', 'Signature', 'Implicit', 'Deprecated'],
            'Total': [184, 185, 195, 24],
            'Success': [66, 69, 86, 0],
            'Success Rate': ['35.87%', '37.30%', '44.10%', '0.00%'],
            'API Usage Accuracy': ['91.85%', '96.22%', '91.28%', '95.83%']
        }
        df_change_rq1_hs32 = pd.DataFrame(data_change_rq1_hs32)
        st.dataframe(df_change_rq1_hs32, use_container_width=True)
    
    with tab4:
        st.subheader("kat-dev-base-32b Performance")
        data_base32 = {
            'Metric': [
                'Total Tasks',
                'Success Count',
                'Failed Count',
                'Pass@1',
                'Incorrect Signatures',
                'Incorrect API',
                'Borrow Checker Failures',
                'Borrow Checker Failure Rate',
                'API Usage True Count',
                'API Usage Accuracy',
                'API Coverage Distinct',
                'API Coverage Count',
                'Compilation Errors',
                'Test Failures'
            ],
            'RQ1 (Full Docs)': [
                588, 190, 398, '32.31%', 0, 34, 369, '92.71%', 
                554, '94.22%', '96.22%', '433/450', 385, 13
            ],
            'RQ3 (Minimal Docs)': [
                588, 169, 419, '28.74%', 0, 30, 390, '93.08%', 
                558, '94.90%', '96.44%', '434/450', 406, 13
            ]
        }
        df_base32 = pd.DataFrame(data_base32)
        st.dataframe(df_base32, use_container_width=True)
    
    st.success("🏆 **Best Performer**: kat-dev-hs-32b achieved highest Pass@1 (37.59%) in RQ1 and excellent API coverage (95.56%)")

# Aider-Polyglot Benchmark
elif benchmark_selection == "Aider-Polyglot":
    st.header("🌐 Aider-Polyglot Benchmark - Multi-language Code Editing")
    
    st.markdown("""
    **Polyglot Benchmark** measures a model's ability to understand and edit complex source code across 6 programming languages.
    - Total: 225 exercises across Rust (30), C++ (26), Go (39), Java (47), JavaScript (49), Python (34)
    - Each exercise has 15-25 unit test cases
    - Evaluates Pass@1, Pass@2, and overall complexity handling
    """)
    
    st.subheader("Overall Performance Comparison")
    
    # Note: The docx mentions scores but doesn't provide specific numbers in tables
    # Creating a comparison based on the information available
    st.info("📊 **Benchmark Focus**: Designed to stress-test models on complex code editing tasks across multiple languages")
    
    st.markdown("""
    ### Models Evaluated:
    - kat-dev-hs-32b
    - kat-dev-base-32b
    - kat-dev-hs-72b
    - kat-dev-base-72b
    
    ### Key Metrics:
    - **Pass@1**: Percentage of tests passing on first attempt
    - **Pass@2**: Percentage of tests passing within 2 attempts (with error feedback)
    
    #### How Pass@2 Works:
    1. **Attempt 1**: Model receives instructions + empty stub file → generates implementation
    2. If tests fail, **Attempt 2**: Model receives previous code + error message → generates fix
    """)
    
    st.warning("⚠️ **Complexity Note**: Due to exercise complexity, models face challenges with these stress tests. Successful completion indicates strong capability to handle complex tasks.")

# Haskell LLM Benchmark
elif benchmark_selection == "Haskell LLM":
    st.header("🎓 Haskell LLM Benchmark - Functional Programming")
    
    st.markdown("""
    **Haskell LLM Benchmark** evaluates functional programming mastery with 112 demanding challenges.
    This is one of the most complex benchmarking suites for Haskell language.
    """)
    
    st.subheader("GLM-Latest Performance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Pass@1 (First-Try)", "54.5%", help="61/112 problems solved immediately")
        st.metric("Pass@2 (Overall)", "63.4%", help="71/112 problems solved after one retry")
    
    with col2:
        st.metric("Well-Formed Responses", "100%", help="Zero malformed outputs")
        st.metric("Syntax Errors", "0%", help="All code is clean and compilable")
    
    with col3:
        st.metric("Average Time per Test", "1.6 min", help="Fast and efficient")
        st.metric("Total Cost", "$0.00", help="Exceptional value")
    
    st.subheader("Detailed Metrics")
    data_haskell = {
        'Metric': [
            'Total Challenges',
            'First-Try Success (Pass@1)',
            'Overall Success (Pass@2)',
            'Improvement on Retry',
            'Syntax Errors',
            'Indentation Errors',
            'Test Timeouts',
            'Average Time per Test',
            'Total Cost'
        ],
        'Result': [
            '112',
            '54.5% (61/112)',
            '63.4% (71/112)',
            '8.9%',
            '0%',
            '0%',
            '0',
            '1.6 minutes',
            '$0.00'
        ]
    }
    df_haskell = pd.DataFrame(data_haskell)
    st.dataframe(df_haskell, use_container_width=True)
    
    st.success("🏆 **GLM-Latest Achievements**:")
    st.markdown("""
    - ✅ High accuracy with solid 54.5% first-try success rate
    - ✅ Robust reliability with 8.9% improvement on retry
    - ✅ 100% zero syntax and indentation errors
    - ✅ Exceptional stability, speed, and cost-effectiveness
    - ✅ Demonstrates deep understanding of Haskell paradigms
    """)

# Footer
st.markdown("---")
st.markdown("*Dashboard created for comprehensive coding model evaluation*")

import time
from subprocess import run,Popen
import streamlit as st








# Streamlit 

backend = st.sidebar.radio('Simulation Backend',['Neuron','NetPyNe'])


pv=st.sidebar.checkbox('Reduce PV')

st.sidebar.write(pv)

pv_percent = st.sidebar.slider('PV Redutcion', 1, 100, 22, 1,disabled = not pv)

sst=st.sidebar.checkbox('Reduce SST')

sst_percent = st.sidebar.slider('SST Redutcion', 1, 100, 40, 1,disabled = not sst)

hostname=run('hostname',capture_output=True).stdout.decode('utf-8')


plot=st.sidebar.checkbox('Produce plots')

st.sidebar.caption('running on ' + hostname.strip() + '@ni')

st.title('Modeling Effects of Inhibition on Schizophrenia')


col1, col2, col3= st.columns(3)





with col1:
    pass
with col2:
    pass

with col2:
    sim_button=st.button('start simulation')
    if sim_button and (('running_experiment' in st.session_state and not st.session_state.running_experiment) or not 'running_experiment' in st.session_state) :
        res=Popen(['mpirun','-errfile-pattern','logs/err.log','-n','28','python' ,'./circuit.py'  ,'--sst' ,str(int(sst)) ,'--sst_percent' , str(sst_percent) , '--pv' , str(int(pv)) , '--pv_percent' ,str(pv_percent) , '--plot' ,str(int(plot))] ,text=True)
        
        pid=res.pid

        st.write('experiment in progress will take approximately 111 minutes')


        st.session_state.pid=pid
        st.session_state.running_experiment=True


        

    if  'running_experiment' in st.session_state:
        if st.session_state.running_experiment:



            stop_sim_button=st.button('stop simulation')

  
         
                
            if stop_sim_button:

                pid=st.session_state.pid
                Popen(['kill','-9',str(pid)])
                st.session_state.running_experiment=False

    # if  'running_experiment' in st.session_state:
    #     if st.session_state.running_experiment:
    #         st.progress(1)
            
          
        





# encoding: utf-8
def Irisfit(sepal_length,sepal_width,petal_length,petal_width):

    import os
    from sklearn.externals import joblib
    import  numpy as np
    from django.conf import settings

    '''machine_file = os.path.join(settings.PROJECT_ROOT,"app", "machine.pkl")
    lr = joblib.load(machine_file)

    if sepal_length and sepal_width and petal_length and petal_width:
        input_value = np.array([sepal_length,sepal_width,petal_length,petal_width],dtype='float')
        y_value = lr.predict(input_value)
        demo_data = 0
    else: #default value for testing
        input_value = []
        y_value = lr.predict(input_value)
        demo_data = 1'''

    #========================================================================

    HTML_text1 =''
    if demo_data:
        HTML_text1 += "<p><p><div class='alert alert-warning' role='alert'>No input data, using demo data set!</div>"

    HTML_text1 +=' <h4>Fitting Model for Iris Experiment</h4>'
    HTML_text1 +="<p>data = %s" % input_value
    HTML_text1 +="<H4>Calculated Target = %f</H4><p>" % y_value
    #========================================================================

    # prepare High Chart , Second block of the result page
    #========================================================================
    HTML_text2 ="<p>feature_names = [sepal_length,sepal_width,petal_length,petal_width]"
    HTML_text2 +="<p>Target = "
    HTML_text2 += "<H4>Provided by Yun-Wen Wang & Teng-Yi Huang</H4>"

    #print HTML
    import Plotting_lib
    chart_title = 'Fitting model for Iris experiment'
    xAxis_label = 'Measured'
    yAxis_label = 'Predicted'
    result_dict = {
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'plot1':Plotting_lib.highchart2(input_value,y_value,xAxis_label,yAxis_label,chart_title),
            'plot2':Plotting_lib.dynamic_svg2(input_value,y_value,xAxis_label,yAxis_label,chart_title),
               }
    return result_dict

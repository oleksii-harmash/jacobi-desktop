matrix_A_temp = []
line_1, line_2, vector = [], [], []
el_2x2_1 = float('2')
el_2x2_2 = float('1')
el_2x2_3 = float('5')
el_2x2_4 = float('7')
el_2x2_5 = float('11')
el_2x2_6 = float('13')
line_1.append(el_2x2_1), line_1.append(el_2x2_2), line_2.append(el_2x2_3), line_2.append(el_2x2_4)
vector.append(el_2x2_5), vector.append(el_2x2_6)
matrix_A_temp.append(line_1), matrix_A_temp.append(line_2)






'''
order = self.ui.comboBox.currentText()
        iterations = self.ui.input_iterations.text()
        matrix_A_temp = self.ui.input_A.toPlainText()
        matrix_B_temp = self.ui.input_B.toPlainText()

        order, iterations = int(order), int(iterations)
        matrix_A, matrix_B, matrix_D_1, matrix_R, result_x, matrix_X_position_zero = [], [], [], [], [], []

        for matrix_A_temp in matrix_A_temp.split('\n'):
            matrix_A.append(matrix_A_temp.split(' '))
        for i in range(order):
            c = 0
            for j in range(order):
                c = float(matrix_A[i][j])
                matrix_A[i][j] = c

'''
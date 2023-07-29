# STUDENT DETAILS STORAGE USING BARCODE OR QRCODE
    #### Video Demo:  <https://youtu.be/VnuxuUWSTwY>
    #### Description:
    The main aspect of this project is to store or display student details to a unique barcode or qrcode.
    This software reads barcode and we can validate,display,append,delete student details to or from it.
    For a student details storage it necessary to have something unique that can represent each student.
    Here we used the barcode or qrcode as the identity of each student.
    For any operation on a perticular student we need to scan the barcode or qrcode first.


    These barcode or qrcode can be either read through video capture or by passing an image.
    It is better to read the qrcode or barcode using videocapture but sometimes we may also
    need to scan .png,.jpeg,.jpg format of barcode images then we use another function that already
    customised here. The student details is stored in a csv file to easy fetch and operation purposes.

    A student has more number of details to store so it is easy to write it as a single row with
    coma seperated. It also uses some voices to indicate certain conditions. This voice indication
    or presentation will gives a better understanding. The displaying of student is done by a tabular method
    and it gives a good final representation and understanding.

    Functions:
        1. Validate
        2. Append
        3. Delete

    Validate is used to validate students is present or not and returns bool value.
    Pretty table is used to organize the student details in tabular format and
    gives better view.




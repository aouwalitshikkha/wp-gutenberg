class WpApi():

    def wpp(text):
        wp_paragaraph = '<!-- wp:paragraph --><p>'+text+'</p><!-- /wp:paragraph -->'
        return wp_paragaraph
    

    def wph2(variable):
        heading2 = '<!-- wp:heading --><h2>' + variable + '</h2><!-- /wp:heading -->'
        return heading2
    
    

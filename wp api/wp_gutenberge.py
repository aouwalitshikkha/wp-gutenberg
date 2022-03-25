class WpApi():

    def wpp(text):
        wp_paragaraph = '<!-- wp:paragraph --><p>'+text+'</p><!-- /wp:paragraph -->'
        return wp_paragaraph
    

    def wph2(text):
        heading2 = '<!-- wp:heading --><h2>' + text + '</h2><!-- /wp:heading -->'
        return heading2
    


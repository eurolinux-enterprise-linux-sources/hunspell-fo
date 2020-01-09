LANG=fo_FO.ISO8859-1

sprog=føroyskt
sprog_en=Faroese
sprog_en_lower_case=faroese
sprogkode=fo
landekode=FO

lang = fo
version = 0.2.37

installdir_old=`locate wordbook/dictionary.lst | sed 's:/dictionary.lst$$::'`
installdir_new=`locate /share/dict/ooo | perl -pe 'use locale; s:^(.*/share/dict/ooo).*$$:$$1:' | sort -u | tail -1`

installdir_user=$(HOME)/.openoffice/user/wordbook

all:

install: $(sprogkode)_$(landekode).dic $(sprogkode)_$(landekode).aff
	if [ -d "$(installdir_old)" ]; then install -o root -g root -m 0644 $(sprogkode)_$(landekode).dic $(installdir_old); echo old location; fi
	if [ -d "$(installdir_old)" ]; then install -o root -g root -m 0644 $(sprogkode)_$(landekode).aff $(installdir_old); echo old location; fi
	if [ -d "$(installdir_new)" ]; then install -o root -g root -m 0644 $(sprogkode)_$(landekode).dic $(installdir_new); echo new location; fi
	if [ -d "$(installdir_new)" ]; then install -o root -g root -m 0644 $(sprogkode)_$(landekode).aff $(installdir_new); echo new location; fi

user_install: $(sprogkode)_$(landekode).dic $(sprogkode)_$(landekode).aff
	@mkdir -p $(installdir_user)
	@if [ -d "$(installdir_user)" ]; then cp -p $(sprogkode)_$(landekode).dic $(sprogkode)_$(landekode).aff $(installdir_user)/; echo DICT el GR $(sprogkode)_$(landekode) >> $(installdir_user)/dictionary.lst; echo DICT $(sprogkode) $(landekode) $(sprogkode)_$(landekode) >> $(installdir_user)/dictionary.lst; echo user location; else echo can not install; exit -1; fi

clean:


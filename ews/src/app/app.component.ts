import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { ButtonModel, ButtonTypeEnum } from '@patterns/button';
import { CardModel } from '@patterns/card';
import { clickListenerEvent, LanguageList, LinkTarget } from '@patterns/common.model';
import { ContentModel } from '@patterns/content';
import { ElementModel, ElementType, SelectOption } from '@patterns/element';
import { FooterModel, FooterTypeEnum } from '@patterns/footer';
import { StringIds } from 'src/stringIds';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'ews';
  card: CardModel;

  model = {
    prop: true,
    first_name: 'Ronak',
    last_name: 'Jain',
    email: 'jainr5668@gmail.com',
  };
  languageModel={
    language:'en'
  }
  button: ButtonModel;
  content: ContentModel = null;
  languageSwitcher: ElementModel;
  languageContainer:ContentModel;
  constructor(public translator: TranslateService) {}
  ngOnInit(): void {
    this.generateLanguageSwitcher()
    this.card = new CardModel();
    this.card.setCardValues(
      'formCard',
      (event) => {
        this.onEventCalled(event);
      },
      StringIds.cHELLO,
      this.generateFooter()
    );
    this.card.content = this.generateContent();
  }

  generateContent(): ContentModel {
    this.content = new ContentModel();
    this.content.setContentValues('card', 'Ronak', null, null);
    this.content.elements = this.generateElements();
    this.content.cols = 3;
    return this.content;
  }

  generateFooter(): FooterModel {
    return new FooterModel(FooterTypeEnum.YES_NO, 'info');
  }
  generateElements(): ElementModel[] {
    const retval: ElementModel[] = [];

    // First Name
    let element: ElementModel = new ElementModel();
    element.textField(
      'first_name',
      StringIds.cFIRSTNAME,
      this.model,
      'first_name'
    );
    element.colspan = 2;
    retval.push(element);

    // Last Name
    element = new ElementModel();
    element.textField(
      'last_name',
      StringIds.clASTNAME,
      this.model,
      'last_name'
    );
    element.colspan = 2;
    retval.push(element);

    // Email
    element = new ElementModel();
    element.email('email', StringIds.cEMAIL, this.model, 'email');
    retval.push(element);

    // Email
    element = new ElementModel();
    element.toggle('toggle', StringIds.cTOGGLE, this.model, 'prop');
    retval.push(element);

    return retval;
  }

  generateLanguageSwitcher() {
    this.languageContainer = new ContentModel();
    this.languageContainer.setContentValues('footer');
    this.languageContainer.elements = [];
    this.languageContainer.cols =12
    const option: SelectOption[] = [];
    for (var language in LanguageList) {
      option.push(
        new SelectOption(LanguageList[language], language)
      );
    }
    this.languageSwitcher = new ElementModel();
    this.languageSwitcher.select(
      'language-selector',
      StringIds.cLANGUAGE,
      this.languageModel,
      'language',
      option,
      (event) => {
        console.log(event);
        this.translator.use(event.event)
      }
    );
    this.languageContainer.elements.push(this.languageSwitcher)
  }
  onEventCalled(event: clickListenerEvent) {
    console.log(event);
    console.log(this.model);
    this.translator.use('de');
  }
}

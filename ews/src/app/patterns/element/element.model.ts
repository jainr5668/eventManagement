export enum ElementType{
    SELECT = 'select',
    TEXT = 'text',
    PASSWORD = 'password',
    TOGGLE = 'toggle',
    EMAIL = 'email'

}
export class SelectOption{
    value: string;
    label: string;
    disabled: boolean;
    constructor(value: string, label:string, disabled?:boolean){
        this.label = label;
        this.value = value;
        this.disabled = disabled;
    }
}
export class ElementModel {
  id: string;
  event: any;
  type: ElementType;
  label: string;
  options: SelectOption[];
  model: any;
  property: string;
  visible: boolean;
  disabled: boolean;
  placeholder: string;
  required: boolean;
  colspan: number;

  private commonProperty(
    id: string,
    label: string,
    model: any,
    property: string,
    event: any,
    colspan: number
  ) {
    this.id = id;
    this.label = label;
    this.model = model;
    this.property = property;
    this.event = event ?? null;
    this.colspan = colspan ?? 1;
  }

  select(
    id: string,
    label: string,
    model: any,
    property: string,
    options: SelectOption[],
    event?: any,
    colspan?: number
  ) {
    this.commonProperty(id, label, model, property, event, colspan);
    this.type = ElementType.SELECT;
    this.options = options;
  }

  textField(
    id: string,
    label: string,
    model: any,
    property: string,
    event?: any,
    colspan?: number
  ) {
    this.commonProperty(id, label, model, property, event, colspan);
    this.type = ElementType.TEXT;
  }

  passwordField(
    id: string,
    label: string,
    model: any,
    property: string,
    event?: any,
    colspan?: number
  ) {
    this.commonProperty(id, label, model, property, event, colspan);
    this.type = ElementType.PASSWORD;
  }

  toggle(
    id: string,
    label: string,
    model: any,
    property: string,
    event?: any,
    colspan?: number
  ) {
    this.commonProperty(id, label, model, property, event, colspan);
    this.type = ElementType.TOGGLE;
  }
  email(
    id: string,
    label: string,
    model: any,
    property: string,
    event?: any,
    colspan?: number
  ) {
    this.commonProperty(id, label, model, property, event,colspan);
    this.type = ElementType.EMAIL;
  }
}